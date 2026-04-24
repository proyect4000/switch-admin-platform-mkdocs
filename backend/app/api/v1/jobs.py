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
