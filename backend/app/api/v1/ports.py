from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.switch_port import SwitchPort
from app.models.switch import Switch
from app.schemas.port import PortCreate, PortUpdate
from app.dependencies import get_current_user, require_permission

router = APIRouter()

@router.get("/switch/{switch_id}")
def list_ports_by_switch(switch_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()
    if not switch:
        raise HTTPException(status_code=404, detail="Switch no encontrado")
    return db.query(SwitchPort).filter(SwitchPort.switch_id == switch_id).order_by(SwitchPort.id.asc()).all()

@router.post("/")
def create_port(payload: PortCreate, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.update"))):
    port = SwitchPort(**payload.dict())
    db.add(port); db.commit(); db.refresh(port)
    return port

@router.put("/{port_id}")
def update_port(port_id: int, payload: PortUpdate, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.update"))):
    port = db.query(SwitchPort).filter(SwitchPort.id == port_id).first()
    if not port:
        raise HTTPException(status_code=404, detail="Puerto no encontrado")
    data = payload.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(port, key, value)
    db.commit(); db.refresh(port)
    return port

@router.delete("/{port_id}")
def delete_port(port_id: int, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.delete"))):
    port = db.query(SwitchPort).filter(SwitchPort.id == port_id).first()
    if not port:
        raise HTTPException(status_code=404, detail="Puerto no encontrado")
    db.delete(port); db.commit()
    return {"message": "Puerto eliminado correctamente"}
