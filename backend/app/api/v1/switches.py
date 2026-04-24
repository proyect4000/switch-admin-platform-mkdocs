from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.crypto import encrypt_value
from app.models.switch import Switch
from app.schemas.switch import SwitchCreate, SwitchUpdate
from app.dependencies import get_current_user, require_permission
from app.services.ssh_service import SSHService
from app.services.audit_service import AuditService

router = APIRouter()

@router.get("/")
def list_switches(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(Switch).filter(Switch.is_deleted == False).order_by(Switch.id.desc()).all()

@router.post("/")
def create_switch(payload: SwitchCreate, request: Request, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.create"))):
    exists = db.query(Switch).filter(Switch.ip_address == str(payload.ip_address)).first()
    if exists:
        raise HTTPException(status_code=400, detail="La IP ya está registrada")
    encrypted_password = encrypt_value(payload.ssh_password) if payload.ssh_password else None
    switch = Switch(
        name=payload.name, hostname=payload.hostname, ip_address=str(payload.ip_address), brand=payload.brand,
        model=payload.model, os_version=payload.os_version, ssh_port=payload.ssh_port,
        ssh_username=payload.ssh_username, ssh_auth_type=payload.ssh_auth_type,
        ssh_password_encrypted=encrypted_password, location=payload.location,
        rack=payload.rack, notes=payload.notes, created_by=current_user.id, status="unknown",
    )
    db.add(switch); db.commit(); db.refresh(switch)
    AuditService.log(db=db, action="CREATE_SWITCH", entity_type="switch", entity_id=switch.id,
                     detail=f"Se creó el switch {switch.name} ({switch.ip_address})",
                     user_id=current_user.id, ip_address=request.client.host if request.client else None)
    return switch

@router.get("/{switch_id}")
def get_switch(switch_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()
    if not switch:
        raise HTTPException(status_code=404, detail="Switch no encontrado")
    return switch

@router.put("/{switch_id}")
def update_switch(switch_id: int, payload: SwitchUpdate, request: Request, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.update"))):
    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()
    if not switch:
        raise HTTPException(status_code=404, detail="Switch no encontrado")
    data = payload.dict(exclude_unset=True)
    if "ssh_password" in data and data["ssh_password"]:
        switch.ssh_password_encrypted = encrypt_value(data.pop("ssh_password"))
    elif "ssh_password" in data:
        data.pop("ssh_password")
    for key, value in data.items():
        setattr(switch, key, value)
    db.commit(); db.refresh(switch)
    AuditService.log(db=db, action="UPDATE_SWITCH", entity_type="switch", entity_id=switch.id,
                     detail=f"Se actualizó el switch {switch.name}", user_id=current_user.id,
                     ip_address=request.client.host if request.client else None)
    return switch

@router.delete("/{switch_id}")
def delete_switch(switch_id: int, request: Request, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.delete"))):
    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()
    if not switch:
        raise HTTPException(status_code=404, detail="Switch no encontrado")
    switch.is_deleted = True
    db.commit()
    AuditService.log(db=db, action="DELETE_SWITCH", entity_type="switch", entity_id=switch.id,
                     detail=f"Se eliminó lógicamente el switch {switch.name}", user_id=current_user.id,
                     ip_address=request.client.host if request.client else None)
    return {"message": "Switch eliminado correctamente"}

@router.post("/{switch_id}/test-ssh")
def test_switch_ssh(switch_id: int, request: Request, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.test_ssh"))):
    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()
    if not switch:
        raise HTTPException(status_code=404, detail="Switch no encontrado")
    if not switch.ssh_password_encrypted:
        raise HTTPException(status_code=400, detail="No hay contraseña SSH configurada")
    ok = SSHService.test_connection(
        host=switch.ip_address, port=switch.ssh_port, username=switch.ssh_username,
        encrypted_password=switch.ssh_password_encrypted
    )
    switch.status = "online" if ok else "offline"
    db.commit()
    AuditService.log(db=db, action="TEST_SSH_SWITCH", entity_type="switch", entity_id=switch.id,
                     detail=f"Prueba SSH: {'OK' if ok else 'ERROR'}", user_id=current_user.id,
                     ip_address=request.client.host if request.client else None)
    return {"connected": ok, "status": switch.status}
