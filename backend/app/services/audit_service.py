from sqlalchemy.orm import Session
from app.models.audit_log import AuditLog

class AuditService:
    @staticmethod
    def log(
        db: Session,
        action: str,
        entity_type: str,
        entity_id: int | None = None,
        detail: str | None = None,
        user_id: int | None = None,
        ip_address: str | None = None,
    ):
        log = AuditLog(
            user_id=user_id,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            detail=detail,
            ip_address=ip_address,
        )
        db.add(log)
        db.commit()
        db.refresh(log)
        return log
