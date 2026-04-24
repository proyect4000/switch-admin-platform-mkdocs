from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.switch import Switch
from app.models.device_link import DeviceLink
from app.models.switch_port import SwitchPort
from app.schemas.topology import LinkCreate, LinkUpdate
from app.dependencies import get_current_user, require_permission

router = APIRouter()

@router.get("/")
def get_topology(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    switches = db.query(Switch).filter(Switch.is_deleted == False).all()
    links = db.query(DeviceLink).all()
    nodes, edges = [], []
    for sw in switches:
        nodes.append({
            "id": sw.id,
            "label": f"{sw.name}\n{sw.ip_address}",
            "group": sw.status,
            "shape": "box",
            "title": f"Marca: {sw.brand or '-'} | Modelo: {sw.model or '-'} | Ubicación: {sw.location or '-'}"
        })
    for link in links:
        source_port = db.query(SwitchPort).filter(SwitchPort.id == link.source_port_id).first() if link.source_port_id else None
        target_port = db.query(SwitchPort).filter(SwitchPort.id == link.target_port_id).first() if link.target_port_id else None
        edges.append({
            "id": link.id,
            "from": link.source_switch_id,
            "to": link.target_switch_id,
            "label": f"{source_port.port_name if source_port else '?'} ↔ {target_port.port_name if target_port else '?'}",
            "status": link.status
        })
    return {"nodes": nodes, "edges": edges}

@router.post("/links")
def create_link(payload: LinkCreate, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.update"))):
    link = DeviceLink(**payload.dict())
    db.add(link); db.commit(); db.refresh(link)
    return link

@router.put("/links/{link_id}")
def update_link(link_id: int, payload: LinkUpdate, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.update"))):
    link = db.query(DeviceLink).filter(DeviceLink.id == link_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="Enlace no encontrado")
    data = payload.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(link, key, value)
    db.commit(); db.refresh(link)
    return link

@router.delete("/links/{link_id}")
def delete_link(link_id: int, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.delete"))):
    link = db.query(DeviceLink).filter(DeviceLink.id == link_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="Enlace no encontrado")
    db.delete(link); db.commit()
    return {"message": "Enlace eliminado correctamente"}
