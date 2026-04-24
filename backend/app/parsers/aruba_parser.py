import re

class ArubaParser:
    @staticmethod
    def parse_interfaces_status(output: str):
        ports = []
        for line in output.splitlines():
            line = line.strip()
            if not line or line.lower().startswith("status") or line.lower().startswith("port"):
                continue
            m = re.match(r"^(\S+)\s+(\S+).*$", line)
            if m:
                state = m.group(2).lower()
                ports.append({
                    "port_name": m.group(1),
                    "oper_status": "up" if state in {"up", "active"} else "down",
                    "admin_status": "up" if state in {"up", "active"} else "down",
                })
        return ports

    @staticmethod
    def parse_lldp_neighbors(output: str):
        neighbors = []
        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) >= 4 and "/" in parts[0]:
                neighbors.append({
                    "local_port": parts[0],
                    "neighbor_name": parts[1],
                    "neighbor_port": parts[-1],
                    "protocol": "LLDP"
                })
        return neighbors

    @staticmethod
    def parse_cdp_neighbors_detail(output: str):
        return []
