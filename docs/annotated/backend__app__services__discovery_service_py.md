# backend/app/services/discovery_service.py

## Propósito

Archivo del proyecto ubicado en `backend/app/services/discovery_service.py`.

## Código fuente

```py
from datetime import datetime
from sqlalchemy.orm import Session

from app.models.switch import Switch
from app.models.switch_port import SwitchPort
from app.models.device_link import DeviceLink
from app.models.device_neighbor import DeviceNeighbor
from app.models.discovery_run import DiscoveryRun
from app.services.ssh_service import SSHService
from app.services.parser_factory import ParserFactory

class DiscoveryService:
    @staticmethod
    def get_commands_by_brand(brand: str | None):
        brand = (brand or "").lower()
        if "cisco" in brand:
            return {
                "ports": ["terminal length 0", "show interfaces status"],
                "lldp": ["terminal length 0", "show lldp neighbors"],
                "cdp": ["terminal length 0", "show cdp neighbors detail"]
            }
        if "aruba" in brand or "hp" in brand:
            return {
                "ports": ["no page", "show interfaces brief"],
                "lldp": ["no page", "show lldp info remote-device"],
                "cdp": []
            }
        return {
            "ports": ["terminal length 0", "show interfaces status"],
            "lldp": ["terminal length 0", "show lldp neighbors"],
            "cdp": []
        }

    @staticmethod
    def sync_ports(db: Session, switch: Switch, parsed_ports: list[dict]) -> int:
        count = 0
        for item in parsed_ports:
            port = db.query(SwitchPort).filter(
                SwitchPort.switch_id == switch.id,
                SwitchPort.port_name == item["port_name"]
            ).first()
            if not port:
                port = SwitchPort(switch_id=switch.id, port_name=item["port_name"])
                db.add(port)
            port.admin_status = item.get("admin_status", "unknown")
            port.oper_status = item.get("oper_status", "unknown")
            count += 1
        db.commit()
        return count

    @staticmethod
    def sync_neighbors(db: Session, switch: Switch, parsed_neighbors: list[dict]) -> int:
        db.query(DeviceNeighbor).filter(DeviceNeighbor.switch_id == switch.id).delete()
        db.commit()
        count = 0
        for item in parsed_neighbors:
            row = DeviceNeighbor(
                switch_id=switch.id,
                local_port=item.get("local_port"),
                neighbor_name=item.get("neighbor_name"),
                neighbor_ip=item.get("neighbor_ip"),
                neighbor_platform=item.get("neighbor_platform"),
                neighbor_port=item.get("neighbor_port"),
                protocol=item.get("protocol"),
            )
            db.add(row)
            count += 1
        db.commit()
        return count

    @staticmethod
    def sync_links(db: Session, switch: Switch) -> int:
        created = 0
        neighbors = db.query(DeviceNeighbor).filter(DeviceNeighbor.switch_id == switch.id).all()
        for neighbor in neighbors:
            remote_switch = None
            if neighbor.neighbor_ip:
                remote_switch = db.query(Switch).filter(
                    Switch.ip_address == neighbor.neighbor_ip,
                    Switch.is_deleted == False
                ).first()
            if not remote_switch and neighbor.neighbor_name:
                remote_switch = db.query(Switch).filter(
                    Switch.name == neighbor.neighbor_name,
                    Switch.is_deleted == False
                ).first()
            if not remote_switch:
                continue

            local_port = db.query(SwitchPort).filter(
                SwitchPort.switch_id == switch.id,
                SwitchPort.port_name == neighbor.local_port
            ).first()
            remote_port = None
            if neighbor.neighbor_port:
                remote_port = db.query(SwitchPort).filter(
                    SwitchPort.switch_id == remote_switch.id,
                    SwitchPort.port_name == neighbor.neighbor_port
                ).first()

            exists = db.query(DeviceLink).filter(
                DeviceLink.source_switch_id == switch.id,
                DeviceLink.target_switch_id == remote_switch.id
            ).first()
            if not exists:
                db.add(DeviceLink(
                    source_switch_id=switch.id,
                    source_port_id=local_port.id if local_port else None,
                    target_switch_id=remote_switch.id,
                    target_port_id=remote_port.id if remote_port else None,
                    link_type="uplink",
                    status="active"
                ))
                created += 1
        db.commit()
        return created

    @staticmethod
    def discover_switch(db: Session, switch: Switch, user_id: int | None = None):
        run = DiscoveryRun(switch_id=switch.id, status="running", created_by=user_id)
        db.add(run)
        db.commit()
        db.refresh(run)
        try:
            commands = DiscoveryService.get_commands_by_brand(switch.brand)
            parser = ParserFactory.get_parser(switch.brand)
            ports_output = SSHService.run_commands_in_shell(switch.ip_address, switch.ssh_port, switch.ssh_username, switch.ssh_password_encrypted, commands["ports"]) if commands["ports"] else ""
            lldp_output = SSHService.run_commands_in_shell(switch.ip_address, switch.ssh_port, switch.ssh_username, switch.ssh_password_encrypted, commands["lldp"]) if commands["lldp"] else ""
            cdp_output = SSHService.run_commands_in_shell(switch.ip_address, switch.ssh_port, switch.ssh_username, switch.ssh_password_encrypted, commands["cdp"]) if commands["cdp"] else ""

            parsed_ports = parser.parse_interfaces_status(ports_output)
            parsed_neighbors = []
            parsed_neighbors.extend(parser.parse_lldp_neighbors(lldp_output))
            if hasattr(parser, "parse_cdp_neighbors_detail"):
                parsed_neighbors.extend(parser.parse_cdp_neighbors_detail(cdp_output))

            ports_updated = DiscoveryService.sync_ports(db, switch, parsed_ports)
            neighbors_detected = DiscoveryService.sync_neighbors(db, switch, parsed_neighbors)
            links_created = DiscoveryService.sync_links(db, switch)

            run.status = "success"
            run.finished_at = datetime.utcnow()
            run.summary = f"Puertos: {ports_updated}, Vecinos: {neighbors_detected}, Enlaces: {links_created}"
            db.commit()
            return {
                "status": "success",
                "ports_updated": ports_updated,
                "neighbors_detected": neighbors_detected,
                "links_created": links_created,
                "summary": run.summary
            }
        except Exception as e:
            run.status = "error"
            run.finished_at = datetime.utcnow()
            run.summary = str(e)
            db.commit()
            return {
                "status": "error",
                "ports_updated": 0,
                "neighbors_detected": 0,
                "links_created": 0,
                "summary": str(e)
            }
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from datetime import datetime` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 4 | `from app.models.switch import Switch` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from app.models.switch_port import SwitchPort` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `from app.models.device_link import DeviceLink` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 7 | `from app.models.device_neighbor import DeviceNeighbor` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `from app.models.discovery_run import DiscoveryRun` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 9 | `from app.services.ssh_service import SSHService` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 10 | `from app.services.parser_factory import ParserFactory` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 11 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 12 | `class DiscoveryService:` | Declara la clase `DiscoveryService` como unidad principal de este bloque. |
| 13 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 14 | `    def get_commands_by_brand(brand: str \| None):` | Declara la función `get_commands_by_brand` con la lógica que se ejecutará cuando sea invocada. |
| 15 | `        brand = (brand or "").lower()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `        if "cisco" in brand:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 17 | `            return {` | Devuelve el resultado de la función al código que la llamó. |
| 18 | `                "ports": ["terminal length 0", "show interfaces status"],` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 19 | `                "lldp": ["terminal length 0", "show lldp neighbors"],` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 20 | `                "cdp": ["terminal length 0", "show cdp neighbors detail"]` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 21 | `            }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 22 | `        if "aruba" in brand or "hp" in brand:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 23 | `            return {` | Devuelve el resultado de la función al código que la llamó. |
| 24 | `                "ports": ["no page", "show interfaces brief"],` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 25 | `                "lldp": ["no page", "show lldp info remote-device"],` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 26 | `                "cdp": []` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 27 | `            }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 28 | `        return {` | Devuelve el resultado de la función al código que la llamó. |
| 29 | `            "ports": ["terminal length 0", "show interfaces status"],` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 30 | `            "lldp": ["terminal length 0", "show lldp neighbors"],` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 31 | `            "cdp": []` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 32 | `        }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 33 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 34 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 35 | `    def sync_ports(db: Session, switch: Switch, parsed_ports: list[dict]) -> int:` | Declara la función `sync_ports` con la lógica que se ejecutará cuando sea invocada. |
| 36 | `        count = 0` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 37 | `        for item in parsed_ports:` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 38 | `            port = db.query(SwitchPort).filter(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 39 | `                SwitchPort.switch_id == switch.id,` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 40 | `                SwitchPort.port_name == item["port_name"]` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 41 | `            ).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 42 | `            if not port:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 43 | `                port = SwitchPort(switch_id=switch.id, port_name=item["port_name"])` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 44 | `                db.add(port)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 45 | `            port.admin_status = item.get("admin_status", "unknown")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 46 | `            port.oper_status = item.get("oper_status", "unknown")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 47 | `            count += 1` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 48 | `        db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 49 | `        return count` | Devuelve el resultado de la función al código que la llamó. |
| 50 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 51 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 52 | `    def sync_neighbors(db: Session, switch: Switch, parsed_neighbors: list[dict]) -> int:` | Declara la función `sync_neighbors` con la lógica que se ejecutará cuando sea invocada. |
| 53 | `        db.query(DeviceNeighbor).filter(DeviceNeighbor.switch_id == switch.id).delete()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 54 | `        db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 55 | `        count = 0` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 56 | `        for item in parsed_neighbors:` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 57 | `            row = DeviceNeighbor(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 58 | `                switch_id=switch.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 59 | `                local_port=item.get("local_port"),` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 60 | `                neighbor_name=item.get("neighbor_name"),` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 61 | `                neighbor_ip=item.get("neighbor_ip"),` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 62 | `                neighbor_platform=item.get("neighbor_platform"),` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 63 | `                neighbor_port=item.get("neighbor_port"),` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 64 | `                protocol=item.get("protocol"),` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 65 | `            )` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 66 | `            db.add(row)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 67 | `            count += 1` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 68 | `        db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 69 | `        return count` | Devuelve el resultado de la función al código que la llamó. |
| 70 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 71 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 72 | `    def sync_links(db: Session, switch: Switch) -> int:` | Declara la función `sync_links` con la lógica que se ejecutará cuando sea invocada. |
| 73 | `        created = 0` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 74 | `        neighbors = db.query(DeviceNeighbor).filter(DeviceNeighbor.switch_id == switch.id).all()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 75 | `        for neighbor in neighbors:` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 76 | `            remote_switch = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 77 | `            if neighbor.neighbor_ip:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 78 | `                remote_switch = db.query(Switch).filter(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 79 | `                    Switch.ip_address == neighbor.neighbor_ip,` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 80 | `                    Switch.is_deleted == False` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 81 | `                ).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 82 | `            if not remote_switch and neighbor.neighbor_name:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 83 | `                remote_switch = db.query(Switch).filter(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 84 | `                    Switch.name == neighbor.neighbor_name,` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 85 | `                    Switch.is_deleted == False` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 86 | `                ).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 87 | `            if not remote_switch:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 88 | `                continue` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 89 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 90 | `            local_port = db.query(SwitchPort).filter(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 91 | `                SwitchPort.switch_id == switch.id,` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 92 | `                SwitchPort.port_name == neighbor.local_port` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 93 | `            ).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 94 | `            remote_port = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 95 | `            if neighbor.neighbor_port:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 96 | `                remote_port = db.query(SwitchPort).filter(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 97 | `                    SwitchPort.switch_id == remote_switch.id,` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 98 | `                    SwitchPort.port_name == neighbor.neighbor_port` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 99 | `                ).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 100 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 101 | `            exists = db.query(DeviceLink).filter(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 102 | `                DeviceLink.source_switch_id == switch.id,` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 103 | `                DeviceLink.target_switch_id == remote_switch.id` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 104 | `            ).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 105 | `            if not exists:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 106 | `                db.add(DeviceLink(` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 107 | `                    source_switch_id=switch.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 108 | `                    source_port_id=local_port.id if local_port else None,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 109 | `                    target_switch_id=remote_switch.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 110 | `                    target_port_id=remote_port.id if remote_port else None,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 111 | `                    link_type="uplink",` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 112 | `                    status="active"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 113 | `                ))` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 114 | `                created += 1` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 115 | `        db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 116 | `        return created` | Devuelve el resultado de la función al código que la llamó. |
| 117 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 118 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 119 | `    def discover_switch(db: Session, switch: Switch, user_id: int \| None = None):` | Declara la función `discover_switch` con la lógica que se ejecutará cuando sea invocada. |
| 120 | `        run = DiscoveryRun(switch_id=switch.id, status="running", created_by=user_id)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 121 | `        db.add(run)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 122 | `        db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 123 | `        db.refresh(run)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 124 | `        try:` | Inicio del manejo controlado de errores para operaciones riesgosas. |
| 125 | `            commands = DiscoveryService.get_commands_by_brand(switch.brand)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 126 | `            parser = ParserFactory.get_parser(switch.brand)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 127 | `            ports_output = SSHService.run_commands_in_shell(switch.ip_address, switch.ssh_port, switch.ssh_username, switch.ssh_password_...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 128 | `            lldp_output = SSHService.run_commands_in_shell(switch.ip_address, switch.ssh_port, switch.ssh_username, switch.ssh_password_e...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 129 | `            cdp_output = SSHService.run_commands_in_shell(switch.ip_address, switch.ssh_port, switch.ssh_username, switch.ssh_password_en...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 130 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 131 | `            parsed_ports = parser.parse_interfaces_status(ports_output)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 132 | `            parsed_neighbors = []` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 133 | `            parsed_neighbors.extend(parser.parse_lldp_neighbors(lldp_output))` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 134 | `            if hasattr(parser, "parse_cdp_neighbors_detail"):` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 135 | `                parsed_neighbors.extend(parser.parse_cdp_neighbors_detail(cdp_output))` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 136 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 137 | `            ports_updated = DiscoveryService.sync_ports(db, switch, parsed_ports)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 138 | `            neighbors_detected = DiscoveryService.sync_neighbors(db, switch, parsed_neighbors)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 139 | `            links_created = DiscoveryService.sync_links(db, switch)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 140 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 141 | `            run.status = "success"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 142 | `            run.finished_at = datetime.utcnow()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 143 | `            run.summary = f"Puertos: {ports_updated}, Vecinos: {neighbors_detected}, Enlaces: {links_created}"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 144 | `            db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 145 | `            return {` | Devuelve el resultado de la función al código que la llamó. |
| 146 | `                "status": "success",` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 147 | `                "ports_updated": ports_updated,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 148 | `                "neighbors_detected": neighbors_detected,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 149 | `                "links_created": links_created,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 150 | `                "summary": run.summary` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 151 | `            }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 152 | `        except Exception as e:` | Captura una excepción específica para responder sin interrumpir toda la aplicación. |
| 153 | `            run.status = "error"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 154 | `            run.finished_at = datetime.utcnow()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 155 | `            run.summary = str(e)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 156 | `            db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 157 | `            return {` | Devuelve el resultado de la función al código que la llamó. |
| 158 | `                "status": "error",` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 159 | `                "ports_updated": 0,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 160 | `                "neighbors_detected": 0,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 161 | `                "links_created": 0,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 162 | `                "summary": str(e)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 163 | `            }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |