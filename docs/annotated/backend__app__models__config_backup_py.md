# backend/app/models/config_backup.py

## Propósito

Archivo del proyecto ubicado en `backend/app/models/config_backup.py`.

## Código fuente

```py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class ConfigBackup(Base):
    __tablename__ = "config_backups"

    id = Column(Integer, primary_key=True, index=True)
    switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)
    backup_type = Column(String(20), nullable=False, default="running-config")
    filename = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.sql import func` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import Base` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `class ConfigBackup(Base):` | Declara la clase `ConfigBackup` como unidad principal de este bloque. |
| 6 | `    __tablename__ = "config_backups"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 8 | `    id = Column(Integer, primary_key=True, index=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    backup_type = Column(String(20), nullable=False, default="running-config")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    filename = Column(String(255), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    content = Column(Text, nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `    created_at = Column(DateTime, server_default=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |