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
