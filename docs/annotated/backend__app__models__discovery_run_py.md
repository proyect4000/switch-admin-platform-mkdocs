# backend/app/models/discovery_run.py

## Propósito

Archivo del proyecto ubicado en `backend/app/models/discovery_run.py`.

## Código fuente

```py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from app.core.database import Base

class DiscoveryRun(Base):
    __tablename__ = "discovery_runs"

    id = Column(Integer, primary_key=True, index=True)
    switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)
    started_at = Column(DateTime, server_default=func.now())
    finished_at = Column(DateTime, nullable=True)
    status = Column(String(20), nullable=False, default="running")
    summary = Column(Text, nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.sql import func` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import Base` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `class DiscoveryRun(Base):` | Declara la clase `DiscoveryRun` como unidad principal de este bloque. |
| 6 | `    __tablename__ = "discovery_runs"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 8 | `    id = Column(Integer, primary_key=True, index=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    started_at = Column(DateTime, server_default=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    finished_at = Column(DateTime, nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    status = Column(String(20), nullable=False, default="running")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `    summary = Column(Text, nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |