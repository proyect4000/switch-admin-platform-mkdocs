# backend/app/schemas/port.py

## Propósito

Archivo del proyecto ubicado en `backend/app/schemas/port.py`.

## Código fuente

```py
from typing import Optional
from pydantic import BaseModel

class PortCreate(BaseModel):
    switch_id: int
    port_name: str
    port_number: Optional[int] = None
    description: Optional[str] = None
    admin_status: str = "down"
    oper_status: str = "down"
    speed: Optional[str] = None
    duplex: Optional[str] = None
    vlan: Optional[str] = None
    mac_address: Optional[str] = None
    connected_device_name: Optional[str] = None
    connected_device_ip: Optional[str] = None

class PortUpdate(BaseModel):
    port_name: Optional[str] = None
    port_number: Optional[int] = None
    description: Optional[str] = None
    admin_status: Optional[str] = None
    oper_status: Optional[str] = None
    speed: Optional[str] = None
    duplex: Optional[str] = None
    vlan: Optional[str] = None
    mac_address: Optional[str] = None
    connected_device_name: Optional[str] = None
    connected_device_ip: Optional[str] = None
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from typing import Optional` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from pydantic import BaseModel` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 4 | `class PortCreate(BaseModel):` | Declara la clase `PortCreate` como unidad principal de este bloque. |
| 5 | `    switch_id: int` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 6 | `    port_name: str` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 7 | `    port_number: Optional[int] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 8 | `    description: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    admin_status: str = "down"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    oper_status: str = "down"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    speed: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    duplex: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `    vlan: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    mac_address: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `    connected_device_name: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `    connected_device_ip: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 18 | `class PortUpdate(BaseModel):` | Declara la clase `PortUpdate` como unidad principal de este bloque. |
| 19 | `    port_name: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `    port_number: Optional[int] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `    description: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `    admin_status: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `    oper_status: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `    speed: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 25 | `    duplex: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 26 | `    vlan: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 27 | `    mac_address: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 28 | `    connected_device_name: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 29 | `    connected_device_ip: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |