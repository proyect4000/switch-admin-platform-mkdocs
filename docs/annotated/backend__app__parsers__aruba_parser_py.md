# backend/app/parsers/aruba_parser.py

## Propósito

Archivo del proyecto ubicado en `backend/app/parsers/aruba_parser.py`.

## Código fuente

```py
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
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `import re` | Importa un módulo o paquete necesario para este archivo. |
| 2 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 3 | `class ArubaParser:` | Declara la clase `ArubaParser` como unidad principal de este bloque. |
| 4 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 5 | `    def parse_interfaces_status(output: str):` | Declara la función `parse_interfaces_status` con la lógica que se ejecutará cuando sea invocada. |
| 6 | `        ports = []` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `        for line in output.splitlines():` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 8 | `            line = line.strip()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `            if not line or line.lower().startswith("status") or line.lower().startswith("port"):` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 10 | `                continue` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 11 | `            m = re.match(r"^(\S+)\s+(\S+).*$", line)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `            if m:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 13 | `                state = m.group(2).lower()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `                ports.append({` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 15 | `                    "port_name": m.group(1),` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 16 | `                    "oper_status": "up" if state in {"up", "active"} else "down",` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 17 | `                    "admin_status": "up" if state in {"up", "active"} else "down",` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 18 | `                })` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 19 | `        return ports` | Devuelve el resultado de la función al código que la llamó. |
| 20 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 21 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 22 | `    def parse_lldp_neighbors(output: str):` | Declara la función `parse_lldp_neighbors` con la lógica que se ejecutará cuando sea invocada. |
| 23 | `        neighbors = []` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `        for line in output.splitlines():` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 25 | `            line = line.strip()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 26 | `            if not line:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 27 | `                continue` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 28 | `            parts = line.split()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 29 | `            if len(parts) >= 4 and "/" in parts[0]:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 30 | `                neighbors.append({` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 31 | `                    "local_port": parts[0],` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 32 | `                    "neighbor_name": parts[1],` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 33 | `                    "neighbor_port": parts[-1],` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 34 | `                    "protocol": "LLDP"` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 35 | `                })` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 36 | `        return neighbors` | Devuelve el resultado de la función al código que la llamó. |
| 37 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 38 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 39 | `    def parse_cdp_neighbors_detail(output: str):` | Declara la función `parse_cdp_neighbors_detail` con la lógica que se ejecutará cuando sea invocada. |
| 40 | `        return []` | Devuelve el resultado de la función al código que la llamó. |