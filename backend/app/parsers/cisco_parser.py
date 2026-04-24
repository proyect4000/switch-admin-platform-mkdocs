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
