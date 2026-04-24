# backend/app/models/ssh_session.py

## Propósito

Archivo del proyecto ubicado en `backend/app/models/ssh_session.py`.

## Código fuente

```py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class SSHSession(Base):
    __tablename__ = "ssh_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    switch_id = Column(Integer, ForeignKey("switches.id"), nullable=False)
    session_uuid = Column(String(100), nullable=False, unique=True)
    client_ip = Column(String(64), nullable=True)
    started_at = Column(DateTime, server_default=func.now())
    ended_at = Column(DateTime, nullable=True)
    status = Column(String(20), nullable=False, default="open")
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from sqlalchemy import Column, Integer, String, DateTime, ForeignKey` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.sql import func` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import Base` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `class SSHSession(Base):` | Declara la clase `SSHSession` como unidad principal de este bloque. |
| 6 | `    __tablename__ = "ssh_sessions"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 8 | `    id = Column(Integer, primary_key=True, index=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    switch_id = Column(Integer, ForeignKey("switches.id"), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    session_uuid = Column(String(100), nullable=False, unique=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    client_ip = Column(String(64), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `    started_at = Column(DateTime, server_default=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    ended_at = Column(DateTime, nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `    status = Column(String(20), nullable=False, default="open")` | Asigna un valor a una variable o atributo para usarlo más adelante. |