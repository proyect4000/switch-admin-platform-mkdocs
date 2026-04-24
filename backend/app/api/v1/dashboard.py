from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.switch import Switch
from app.models.discovery_run import DiscoveryRun
from app.models.config_backup import ConfigBackup
from app.dependencies import get_current_user

router = APIRouter()

@router.get("/summary")
def get_dashboard_summary(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    total = db.query(Switch).filter(Switch.is_deleted == False).count()
    online = db.query(Switch).filter(Switch.is_deleted == False, Switch.status == "online").count()
    offline = db.query(Switch).filter(Switch.is_deleted == False, Switch.status == "offline").count()
    discoveries_ok = db.query(DiscoveryRun).filter(DiscoveryRun.status == "success").count()
    discoveries_error = db.query(DiscoveryRun).filter(DiscoveryRun.status == "error").count()
    backups_total = db.query(ConfigBackup).count()
    return {
        "total_switches": total,
        "online_switches": online,
        "offline_switches": offline,
        "discovery_success": discoveries_ok,
        "discovery_error": discoveries_error,
        "backups_total": backups_total
    }
