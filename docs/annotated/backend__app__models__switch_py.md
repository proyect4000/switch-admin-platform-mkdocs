# backend/app/models/switch.py

## Propósito

Archivo del proyecto ubicado en `backend/app/models/switch.py`.

## Código fuente

```py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Switch(Base):
    __tablename__ = "switches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    hostname = Column(String(150), nullable=True)
    ip_address = Column(String(45), unique=True, nullable=False, index=True)
    brand = Column(String(80), nullable=True)
    model = Column(String(100), nullable=True)
    os_version = Column(String(100), nullable=True)
    ssh_port = Column(Integer, nullable=False, default=22)
    ssh_username = Column(String(100), nullable=False)
    ssh_auth_type = Column(String(20), nullable=False, default="password")
    ssh_password_encrypted = Column(String, nullable=True)
    ssh_private_key_encrypted = Column(String, nullable=True)
    location = Column(String(150), nullable=True)
    rack = Column(String(100), nullable=True)
    notes = Column(String, nullable=True)
    status = Column(String(20), nullable=False, default="unknown")
    is_deleted = Column(Boolean, nullable=False, default=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.sql import func` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import Base` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `class Switch(Base):` | Declara la clase `Switch` como unidad principal de este bloque. |
| 6 | `    __tablename__ = "switches"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 8 | `    id = Column(Integer, primary_key=True, index=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    name = Column(String(150), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    hostname = Column(String(150), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    ip_address = Column(String(45), unique=True, nullable=False, index=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    brand = Column(String(80), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `    model = Column(String(100), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    os_version = Column(String(100), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `    ssh_port = Column(Integer, nullable=False, default=22)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `    ssh_username = Column(String(100), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `    ssh_auth_type = Column(String(20), nullable=False, default="password")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 18 | `    ssh_password_encrypted = Column(String, nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 19 | `    ssh_private_key_encrypted = Column(String, nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `    location = Column(String(150), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `    rack = Column(String(100), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `    notes = Column(String, nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `    status = Column(String(20), nullable=False, default="unknown")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `    is_deleted = Column(Boolean, nullable=False, default=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 25 | `    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 26 | `    created_at = Column(DateTime, server_default=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 27 | `    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |