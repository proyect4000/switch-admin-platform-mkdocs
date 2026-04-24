# backend/app/services/scheduler_service.py

## Propósito

Archivo del proyecto ubicado en `backend/app/services/scheduler_service.py`.

## Código fuente

```py
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.scheduled_job import ScheduledJob
from app.models.switch import Switch
from app.services.discovery_service import DiscoveryService
from app.services.backup_service import BackupService
from app.utils.cron_utils import parse_simple_cron

scheduler = BackgroundScheduler()

def job_run_discovery(switch_id: int):
    db: Session = SessionLocal()
    try:
        sw = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()
        if sw:
            DiscoveryService.discover_switch(db, sw, None)
    finally:
        db.close()

def job_run_backup(switch_id: int):
    db: Session = SessionLocal()
    try:
        sw = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()
        if sw:
            BackupService.run_backup(db, sw, "running-config", None)
    finally:
        db.close()

def sync_jobs():
    db: Session = SessionLocal()
    try:
        for job in scheduler.get_jobs():
            scheduler.remove_job(job.id)
        jobs = db.query(ScheduledJob).filter(ScheduledJob.is_active == True).all()
        for scheduled in jobs:
            trigger_args = parse_simple_cron(scheduled.cron_expression)
            job_id = f"{scheduled.job_type}_{scheduled.id}"
            if scheduled.job_type == "discovery":
                scheduler.add_job(job_run_discovery, trigger="cron", id=job_id, replace_existing=True, args=[scheduled.target_switch_id], **trigger_args)
            elif scheduled.job_type == "backup":
                scheduler.add_job(job_run_backup, trigger="cron", id=job_id, replace_existing=True, args=[scheduled.target_switch_id], **trigger_args)
    finally:
        db.close()

def start_scheduler():
    if not scheduler.running:
        sync_jobs()
        scheduler.start()
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from apscheduler.schedulers.background import BackgroundScheduler` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 4 | `from app.core.database import SessionLocal` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from app.models.scheduled_job import ScheduledJob` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `from app.models.switch import Switch` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 7 | `from app.services.discovery_service import DiscoveryService` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `from app.services.backup_service import BackupService` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 9 | `from app.utils.cron_utils import parse_simple_cron` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 10 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 11 | `scheduler = BackgroundScheduler()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 13 | `def job_run_discovery(switch_id: int):` | Declara la función `job_run_discovery` con la lógica que se ejecutará cuando sea invocada. |
| 14 | `    db: Session = SessionLocal()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `    try:` | Inicio del manejo controlado de errores para operaciones riesgosas. |
| 16 | `        sw = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 17 | `        if sw:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 18 | `            DiscoveryService.discover_switch(db, sw, None)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 19 | `    finally:` | Bloque de cierre que se ejecuta siempre, útil para liberar recursos. |
| 20 | `        db.close()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 21 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 22 | `def job_run_backup(switch_id: int):` | Declara la función `job_run_backup` con la lógica que se ejecutará cuando sea invocada. |
| 23 | `    db: Session = SessionLocal()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `    try:` | Inicio del manejo controlado de errores para operaciones riesgosas. |
| 25 | `        sw = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 26 | `        if sw:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 27 | `            BackupService.run_backup(db, sw, "running-config", None)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 28 | `    finally:` | Bloque de cierre que se ejecuta siempre, útil para liberar recursos. |
| 29 | `        db.close()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 30 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 31 | `def sync_jobs():` | Declara la función `sync_jobs` con la lógica que se ejecutará cuando sea invocada. |
| 32 | `    db: Session = SessionLocal()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 33 | `    try:` | Inicio del manejo controlado de errores para operaciones riesgosas. |
| 34 | `        for job in scheduler.get_jobs():` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 35 | `            scheduler.remove_job(job.id)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 36 | `        jobs = db.query(ScheduledJob).filter(ScheduledJob.is_active == True).all()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 37 | `        for scheduled in jobs:` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 38 | `            trigger_args = parse_simple_cron(scheduled.cron_expression)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 39 | `            job_id = f"{scheduled.job_type}_{scheduled.id}"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 40 | `            if scheduled.job_type == "discovery":` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 41 | `                scheduler.add_job(job_run_discovery, trigger="cron", id=job_id, replace_existing=True, args=[scheduled.target_switch_id],...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 42 | `            elif scheduled.job_type == "backup":` | Condición alternativa que se evalúa si la anterior no se cumple. |
| 43 | `                scheduler.add_job(job_run_backup, trigger="cron", id=job_id, replace_existing=True, args=[scheduled.target_switch_id], **...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 44 | `    finally:` | Bloque de cierre que se ejecuta siempre, útil para liberar recursos. |
| 45 | `        db.close()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 46 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 47 | `def start_scheduler():` | Declara la función `start_scheduler` con la lógica que se ejecutará cuando sea invocada. |
| 48 | `    if not scheduler.running:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 49 | `        sync_jobs()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 50 | `        scheduler.start()` | Línea de implementación que forma parte del comportamiento interno del archivo. |