# backend/app/models/scheduled_job.py

## Propósito

Archivo del proyecto ubicado en `backend/app/models/scheduled_job.py`.

## Código fuente

```py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class ScheduledJob(Base):
    __tablename__ = "scheduled_jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_name = Column(String(120), nullable=False)
    job_type = Column(String(50), nullable=False)
    cron_expression = Column(String(100), nullable=False)
    target_switch_id = Column(Integer, ForeignKey("switches.id"), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    last_run_at = Column(DateTime, nullable=True)
    next_run_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.sql import func` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import Base` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `class ScheduledJob(Base):` | Declara la clase `ScheduledJob` como unidad principal de este bloque. |
| 6 | `    __tablename__ = "scheduled_jobs"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 8 | `    id = Column(Integer, primary_key=True, index=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    job_name = Column(String(120), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    job_type = Column(String(50), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    cron_expression = Column(String(100), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    target_switch_id = Column(Integer, ForeignKey("switches.id"), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `    is_active = Column(Boolean, nullable=False, default=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    last_run_at = Column(DateTime, nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `    next_run_at = Column(DateTime, nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `    created_at = Column(DateTime, server_default=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |