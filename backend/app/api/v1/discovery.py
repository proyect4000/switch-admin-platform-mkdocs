from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.switch import Switch
from app.models.device_neighbor import DeviceNeighbor
from app.models.discovery_run import DiscoveryRun
from app.dependencies import get_current_user, require_permission
from app.services.discovery_service import DiscoveryService
from app.services.audit_service import AuditService

router = APIRouter()

@router.post("/switches/{switch_id}/run")
def run_discovery(switch_id: int, request: Request, db: Session = Depends(get_db), current_user=Depends(require_permission("discovery.run"))):
    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()
    if not switch:
        raise HTTPException(status_code=404, detail="Switch no encontrado")
    if not switch.ssh_password_encrypted:
        raise HTTPException(status_code=400, detail="El switch no tiene credenciales SSH")
    result = DiscoveryService.discover_switch(db=db, switch=switch, user_id=current_user.id)
    AuditService.log(db=db, action="RUN_DISCOVERY", entity_type="switch", entity_id=switch.id,
                     detail=result["summary"], user_id=current_user.id,
                     ip_address=request.client.host if request.client else None)
    return result

@router.get("/switches/{switch_id}/neighbors")
def get_neighbors(switch_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(DeviceNeighbor).filter(DeviceNeighbor.switch_id == switch_id).order_by(DeviceNeighbor.id.desc()).all()

@router.get("/switches/{switch_id}/runs")
def get_discovery_runs(switch_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(DiscoveryRun).filter(DiscoveryRun.switch_id == switch_id).order_by(DiscoveryRun.started_at.desc()).all()
