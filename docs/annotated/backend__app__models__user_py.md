# backend/app/models/user.py

## Propósito

Archivo del proyecto ubicado en `backend/app/models/user.py`.

## Código fuente

```py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(80), unique=True, nullable=False, index=True)
    full_name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String(30), nullable=False, default="operator")
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from sqlalchemy import Column, Integer, String, Boolean, DateTime` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.sql import func` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import Base` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `class User(Base):` | Declara la clase `User` como unidad principal de este bloque. |
| 6 | `    __tablename__ = "users"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 8 | `    id = Column(Integer, primary_key=True, index=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    username = Column(String(80), unique=True, nullable=False, index=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    full_name = Column(String(150), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    email = Column(String(150), unique=True, nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    password_hash = Column(String, nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `    role = Column(String(30), nullable=False, default="operator")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    is_active = Column(Boolean, nullable=False, default=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `    created_at = Column(DateTime, server_default=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |