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
