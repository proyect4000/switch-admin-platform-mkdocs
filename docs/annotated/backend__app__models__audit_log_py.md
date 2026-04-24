# backend/app/models/audit_log.py

## Propósito

Archivo del proyecto ubicado en `backend/app/models/audit_log.py`.

## Código fuente

```py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    action = Column(String(100), nullable=False)
    entity_type = Column(String(50), nullable=False)
    entity_id = Column(Integer, nullable=True)
    detail = Column(Text, nullable=True)
    ip_address = Column(String(64), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.sql import func` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import Base` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `class AuditLog(Base):` | Declara la clase `AuditLog` como unidad principal de este bloque. |
| 6 | `    __tablename__ = "audit_logs"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 8 | `    id = Column(Integer, primary_key=True, index=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    action = Column(String(100), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    entity_type = Column(String(50), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    entity_id = Column(Integer, nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `    detail = Column(Text, nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    ip_address = Column(String(64), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `    created_at = Column(DateTime, server_default=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |