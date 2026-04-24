# backend/app/schemas/job.py

## Propósito

Archivo del proyecto ubicado en `backend/app/schemas/job.py`.

## Código fuente

```py
from typing import Optional
from pydantic import BaseModel

class JobCreate(BaseModel):
    job_name: str
    job_type: str
    cron_expression: str
    target_switch_id: Optional[int] = None
    is_active: bool = True
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from typing import Optional` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from pydantic import BaseModel` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 4 | `class JobCreate(BaseModel):` | Declara la clase `JobCreate` como unidad principal de este bloque. |
| 5 | `    job_name: str` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 6 | `    job_type: str` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 7 | `    cron_expression: str` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 8 | `    target_switch_id: Optional[int] = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    is_active: bool = True` | Asigna un valor a una variable o atributo para usarlo más adelante. |