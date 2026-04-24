# backend/app/api/v1/jobs.py

## Propósito

Archivo del proyecto ubicado en `backend/app/api/v1/jobs.py`.

## Código fuente

```py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.scheduled_job import ScheduledJob
from app.schemas.job import JobCreate
from app.dependencies import require_permission
from app.services.scheduler_service import sync_jobs

router = APIRouter()

@router.get("/")
def list_jobs(db: Session = Depends(get_db), current_user=Depends(require_permission("job.manage"))):
    return db.query(ScheduledJob).order_by(ScheduledJob.created_at.desc()).all()

@router.post("/")
def create_job(payload: JobCreate, db: Session = Depends(get_db), current_user=Depends(require_permission("job.manage"))):
    job = ScheduledJob(
        job_name=payload.job_name,
        job_type=payload.job_type,
        cron_expression=payload.cron_expression,
        target_switch_id=payload.target_switch_id,
        is_active=payload.is_active,
        created_by=current_user.id
    )
    db.add(job); db.commit(); db.refresh(job)
    sync_jobs()
    return job

@router.put("/{job_id}/toggle")
def toggle_job(job_id: int, db: Session = Depends(get_db), current_user=Depends(require_permission("job.manage"))):
    job = db.query(ScheduledJob).filter(ScheduledJob.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job no encontrado")
    job.is_active = not job.is_active
    db.commit()
    sync_jobs()
    return {"id": job.id, "is_active": job.is_active}
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from fastapi import APIRouter, Depends, HTTPException` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import get_db` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from app.models.scheduled_job import ScheduledJob` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from app.schemas.job import JobCreate` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `from app.dependencies import require_permission` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 7 | `from app.services.scheduler_service import sync_jobs` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 9 | `router = APIRouter()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 11 | `@router.get("/")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 12 | `def list_jobs(db: Session = Depends(get_db), current_user=Depends(require_permission("job.manage"))):` | Declara la función `list_jobs` con la lógica que se ejecutará cuando sea invocada. |
| 13 | `    return db.query(ScheduledJob).order_by(ScheduledJob.created_at.desc()).all()` | Devuelve el resultado de la función al código que la llamó. |
| 14 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 15 | `@router.post("/")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 16 | `def create_job(payload: JobCreate, db: Session = Depends(get_db), current_user=Depends(require_permission("job.manage"))):` | Declara la función `create_job` con la lógica que se ejecutará cuando sea invocada. |
| 17 | `    job = ScheduledJob(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 18 | `        job_name=payload.job_name,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 19 | `        job_type=payload.job_type,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `        cron_expression=payload.cron_expression,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `        target_switch_id=payload.target_switch_id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `        is_active=payload.is_active,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `        created_by=current_user.id` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `    )` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 25 | `    db.add(job); db.commit(); db.refresh(job)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 26 | `    sync_jobs()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 27 | `    return job` | Devuelve el resultado de la función al código que la llamó. |
| 28 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 29 | `@router.put("/{job_id}/toggle")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 30 | `def toggle_job(job_id: int, db: Session = Depends(get_db), current_user=Depends(require_permission("job.manage"))):` | Declara la función `toggle_job` con la lógica que se ejecutará cuando sea invocada. |
| 31 | `    job = db.query(ScheduledJob).filter(ScheduledJob.id == job_id).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 32 | `    if not job:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 33 | `        raise HTTPException(status_code=404, detail="Job no encontrado")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 34 | `    job.is_active = not job.is_active` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 35 | `    db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 36 | `    sync_jobs()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 37 | `    return {"id": job.id, "is_active": job.is_active}` | Devuelve el resultado de la función al código que la llamó. |