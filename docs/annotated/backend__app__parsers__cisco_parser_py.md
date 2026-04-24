# backend/app/parsers/cisco_parser.py

## Propósito

Archivo del proyecto ubicado en `backend/app/parsers/cisco_parser.py`.

## Código fuente

```py
import re

class CiscoParser:
    @staticmethod
    def parse_interfaces_status(output: str):
        ports = []
        for line in output.splitlines():
            line = line.strip()
            if not line or line.lower().startswith("port "):
                continue
            m = re.match(r"^(\S+)\s+(\S+)\s+.*$", line)
            if m:
                port_name = m.group(1)
                raw_status = m.group(2).lower()
                if raw_status == "connected":
                    oper_status = "up"
                    admin_status = "up"
                elif raw_status in {"notconnect", "disabled", "inactive", "err-disabled"}:
                    oper_status = "down"
                    admin_status = "down"
                else:
                    oper_status = "unknown"
                    admin_status = "unknown"
                ports.append({"port_name": port_name, "oper_status": oper_status, "admin_status": admin_status})
        return ports

    @staticmethod
    def parse_lldp_neighbors(output: str):
        neighbors = []
        for line in output.splitlines():
            line = line.strip()
            if not line or "Device ID" in line or "Local Intf" in line:
                continue
            parts = line.split()
            if len(parts) >= 4:
                neighbors.append({
                    "neighbor_name": parts[0],
                    "local_port": parts[1],
                    "neighbor_port": parts[-1],
                    "protocol": "LLDP"
                })
        return neighbors

    @staticmethod
    def parse_cdp_neighbors_detail(output: str):
        neighbors = []
        blocks = output.split("-------------------------")
        for block in blocks:
            item = {}
            patterns = {
                "neighbor_name": r"Device ID:\s*(.+)",
                "neighbor_ip": r"IP address:\s*(.+)",
                "neighbor_platform": r"Platform:\s*(.+?),",
                "local_port": r"Interface:\s*(.+?),",
                "neighbor_port": r"Port ID \(outgoing port\):\s*(.+)",
            }
            for key, pat in patterns.items():
                m = re.search(pat, block)
                if m:
                    item[key] = m.group(1).strip()
            if item.get("neighbor_name") and item.get("local_port"):
                item["protocol"] = "CDP"
                neighbors.append(item)
        return neighbors
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `import re` | Importa un módulo o paquete necesario para este archivo. |
| 2 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 3 | `class CiscoParser:` | Declara la clase `CiscoParser` como unidad principal de este bloque. |
| 4 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 5 | `    def parse_interfaces_status(output: str):` | Declara la función `parse_interfaces_status` con la lógica que se ejecutará cuando sea invocada. |
| 6 | `        ports = []` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `        for line in output.splitlines():` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 8 | `            line = line.strip()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `            if not line or line.lower().startswith("port "):` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 10 | `                continue` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 11 | `            m = re.match(r"^(\S+)\s+(\S+)\s+.*$", line)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `            if m:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 13 | `                port_name = m.group(1)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `                raw_status = m.group(2).lower()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `                if raw_status == "connected":` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 16 | `                    oper_status = "up"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `                    admin_status = "up"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 18 | `                elif raw_status in {"notconnect", "disabled", "inactive", "err-disabled"}:` | Condición alternativa que se evalúa si la anterior no se cumple. |
| 19 | `                    oper_status = "down"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `                    admin_status = "down"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `                else:` | Bloque alternativo que se ejecuta cuando no se cumplen las condiciones previas. |
| 22 | `                    oper_status = "unknown"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `                    admin_status = "unknown"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `                ports.append({"port_name": port_name, "oper_status": oper_status, "admin_status": admin_status})` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 25 | `        return ports` | Devuelve el resultado de la función al código que la llamó. |
| 26 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 27 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 28 | `    def parse_lldp_neighbors(output: str):` | Declara la función `parse_lldp_neighbors` con la lógica que se ejecutará cuando sea invocada. |
| 29 | `        neighbors = []` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 30 | `        for line in output.splitlines():` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 31 | `            line = line.strip()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 32 | `            if not line or "Device ID" in line or "Local Intf" in line:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 33 | `                continue` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 34 | `            parts = line.split()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 35 | `            if len(parts) >= 4:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 36 | `                neighbors.append({` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 37 | `                    "neighbor_name": parts[0],` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 38 | `                    "local_port": parts[1],` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 39 | `                    "neighbor_port": parts[-1],` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 40 | `                    "protocol": "LLDP"` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 41 | `                })` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 42 | `        return neighbors` | Devuelve el resultado de la función al código que la llamó. |
| 43 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 44 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 45 | `    def parse_cdp_neighbors_detail(output: str):` | Declara la función `parse_cdp_neighbors_detail` con la lógica que se ejecutará cuando sea invocada. |
| 46 | `        neighbors = []` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 47 | `        blocks = output.split("-------------------------")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 48 | `        for block in blocks:` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 49 | `            item = {}` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 50 | `            patterns = {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 51 | `                "neighbor_name": r"Device ID:\s*(.+)",` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 52 | `                "neighbor_ip": r"IP address:\s*(.+)",` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 53 | `                "neighbor_platform": r"Platform:\s*(.+?),",` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 54 | `                "local_port": r"Interface:\s*(.+?),",` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 55 | `                "neighbor_port": r"Port ID \(outgoing port\):\s*(.+)",` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 56 | `            }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 57 | `            for key, pat in patterns.items():` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 58 | `                m = re.search(pat, block)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 59 | `                if m:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 60 | `                    item[key] = m.group(1).strip()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 61 | `            if item.get("neighbor_name") and item.get("local_port"):` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 62 | `                item["protocol"] = "CDP"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 63 | `                neighbors.append(item)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 64 | `        return neighbors` | Devuelve el resultado de la función al código que la llamó. |