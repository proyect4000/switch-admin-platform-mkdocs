# backend/app/schemas/auth.py

## Propósito

Archivo del proyecto ubicado en `backend/app/schemas/auth.py`.

## Código fuente

```py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    password: str
    role: str = "operator"
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from pydantic import BaseModel, EmailStr` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 3 | `class UserCreate(BaseModel):` | Declara la clase `UserCreate` como unidad principal de este bloque. |
| 4 | `    username: str` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 5 | `    full_name: str` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 6 | `    email: EmailStr` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 7 | `    password: str` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 8 | `    role: str = "operator"` | Asigna un valor a una variable o atributo para usarlo más adelante. |