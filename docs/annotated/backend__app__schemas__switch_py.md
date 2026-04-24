# backend/app/schemas/switch.py

## Propósito

Archivo del proyecto ubicado en `backend/app/schemas/switch.py`.

## Código fuente

```py
from typing import Optional
from pydantic import BaseModel, IPvAnyAddress

class SwitchCreate(BaseModel):
    name: str
    hostname: Optional[str] = None
    ip_address: IPvAnyAddress
    brand: Optional[str] = None
    model: Optional[str] = None
    os_version: Optional[str] = None
    ssh_port: int = 22
    ssh_username: str
    ssh_password: Optional[str] = None
    ssh_auth_type: str = "password"
    location: Optional[str] = None
    rack: Optional[str] = None
    notes: Optional[str] = None

class SwitchUpdate(BaseModel):
    name: Optional[str] = None
    hostname: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    os_version: Optional[str] = None
    ssh_port: Optional[int] = None
    ssh_username: Optional[str] = None
    ssh_password: Optional[str] = None
    ssh_auth_type: Optional[str] = None
    location: Optional[str] = None
    rack: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[str] = None
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from typing import Optional` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from pydantic import BaseModel, IPvAnyAddress` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 4 | `class SwitchCreate(BaseModel):` | Declara la clase `SwitchCreate` como unidad principal de este bloque. |
| 5 | `    name: str` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 6 | `    hostname: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `    ip_address: IPvAnyAddress` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 8 | `    brand: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    model: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    os_version: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    ssh_port: int = 22` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    ssh_username: str` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 13 | `    ssh_password: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    ssh_auth_type: str = "password"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `    location: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `    rack: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `    notes: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 18 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 19 | `class SwitchUpdate(BaseModel):` | Declara la clase `SwitchUpdate` como unidad principal de este bloque. |
| 20 | `    name: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `    hostname: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `    brand: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `    model: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `    os_version: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 25 | `    ssh_port: Optional[int] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 26 | `    ssh_username: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 27 | `    ssh_password: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 28 | `    ssh_auth_type: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 29 | `    location: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 30 | `    rack: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 31 | `    notes: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 32 | `    status: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |