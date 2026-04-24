# backend/app/schemas/topology.py

## Propósito

Archivo del proyecto ubicado en `backend/app/schemas/topology.py`.

## Código fuente

```py
from typing import Optional
from pydantic import BaseModel

class LinkCreate(BaseModel):
    source_switch_id: int
    source_port_id: Optional[int] = None
    target_switch_id: int
    target_port_id: Optional[int] = None
    link_type: str = "uplink"
    status: str = "active"

class LinkUpdate(BaseModel):
    source_port_id: Optional[int] = None
    target_port_id: Optional[int] = None
    link_type: Optional[str] = None
    status: Optional[str] = None
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from typing import Optional` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from pydantic import BaseModel` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 4 | `class LinkCreate(BaseModel):` | Declara la clase `LinkCreate` como unidad principal de este bloque. |
| 5 | `    source_switch_id: int` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 6 | `    source_port_id: Optional[int] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `    target_switch_id: int` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 8 | `    target_port_id: Optional[int] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    link_type: str = "uplink"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    status: str = "active"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 12 | `class LinkUpdate(BaseModel):` | Declara la clase `LinkUpdate` como unidad principal de este bloque. |
| 13 | `    source_port_id: Optional[int] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    target_port_id: Optional[int] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `    link_type: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `    status: Optional[str] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |