from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.switch import Switch
from app.models.config_backup import ConfigBackup
from app.dependencies import require_permission
from app.services.backup_service import BackupService
from app.services.audit_service import AuditService

router = APIRouter()

@router.post("/switches/{switch_id}/run")
def run_backup(switch_id: int, request: Request, backup_type: str = "running-config", db: Session = Depends(get_db), current_user=Depends(require_permission("backup.run"))):
    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()
    if not switch:
        raise HTTPException(status_code=404, detail="Switch no encontrado")
    backup = BackupService.run_backup(db, switch, backup_type, current_user.id)
    AuditService.log(db=db, action="RUN_BACKUP", entity_type="switch", entity_id=switch.id,
                     detail=f"Backup generado: {backup.filename}", user_id=current_user.id,
                     ip_address=request.client.host if request.client else None)
    return backup

@router.get("/switches/{switch_id}")
def list_backups(switch_id: int, db: Session = Depends(get_db), current_user=Depends(require_permission("backup.download"))):
    return db.query(ConfigBackup).filter(ConfigBackup.switch_id == switch_id).order_by(ConfigBackup.created_at.desc()).all()

@router.get("/{backup_id}")
def get_backup(backup_id: int, db: Session = Depends(get_db), current_user=Depends(require_permission("backup.download"))):
    backup = db.query(ConfigBackup).filter(ConfigBackup.id == backup_id).first()
    if not backup:
        raise HTTPException(status_code=404, detail="Backup no encontrado")
    return backup
