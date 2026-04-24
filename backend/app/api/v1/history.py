from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.ssh_session import SSHSession
from app.models.ssh_command import SSHCommand
from app.models.audit_log import AuditLog
from app.dependencies import require_permission

router = APIRouter()

@router.get("/sessions")
def list_ssh_sessions(db: Session = Depends(get_db), current_user=Depends(require_permission("audit.read"))):
    return db.query(SSHSession).order_by(SSHSession.started_at.desc()).all()

@router.get("/commands")
def list_ssh_commands(db: Session = Depends(get_db), current_user=Depends(require_permission("audit.read"))):
    return db.query(SSHCommand).order_by(SSHCommand.executed_at.desc()).all()

@router.get("/audit-logs")
def list_audit_logs(db: Session = Depends(get_db), current_user=Depends(require_permission("audit.read"))):
    return db.query(AuditLog).order_by(AuditLog.created_at.desc()).all()
