# backend/app/api/v1/switches.py

## Propósito

Archivo del proyecto ubicado en `backend/app/api/v1/switches.py`.

## Código fuente

```py
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
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from fastapi import APIRouter, Depends, HTTPException, Request` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import get_db` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from app.core.crypto import encrypt_value` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from app.models.switch import Switch` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `from app.schemas.switch import SwitchCreate, SwitchUpdate` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 7 | `from app.dependencies import get_current_user, require_permission` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `from app.services.ssh_service import SSHService` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 9 | `from app.services.audit_service import AuditService` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 10 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 11 | `router = APIRouter()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 13 | `@router.get("/")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 14 | `def list_switches(db: Session = Depends(get_db), current_user=Depends(get_current_user)):` | Declara la función `list_switches` con la lógica que se ejecutará cuando sea invocada. |
| 15 | `    return db.query(Switch).filter(Switch.is_deleted == False).order_by(Switch.id.desc()).all()` | Devuelve el resultado de la función al código que la llamó. |
| 16 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 17 | `@router.post("/")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 18 | `def create_switch(payload: SwitchCreate, request: Request, db: Session = Depends(get_db), current_user=Depends(require_permission("switch...` | Declara la función `create_switch` con la lógica que se ejecutará cuando sea invocada. |
| 19 | `    exists = db.query(Switch).filter(Switch.ip_address == str(payload.ip_address)).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 20 | `    if exists:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 21 | `        raise HTTPException(status_code=400, detail="La IP ya está registrada")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 22 | `    encrypted_password = encrypt_value(payload.ssh_password) if payload.ssh_password else None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `    switch = Switch(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `        name=payload.name, hostname=payload.hostname, ip_address=str(payload.ip_address), brand=payload.brand,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 25 | `        model=payload.model, os_version=payload.os_version, ssh_port=payload.ssh_port,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 26 | `        ssh_username=payload.ssh_username, ssh_auth_type=payload.ssh_auth_type,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 27 | `        ssh_password_encrypted=encrypted_password, location=payload.location,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 28 | `        rack=payload.rack, notes=payload.notes, created_by=current_user.id, status="unknown",` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 29 | `    )` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 30 | `    db.add(switch); db.commit(); db.refresh(switch)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 31 | `    AuditService.log(db=db, action="CREATE_SWITCH", entity_type="switch", entity_id=switch.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 32 | `                     detail=f"Se creó el switch {switch.name} ({switch.ip_address})",` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 33 | `                     user_id=current_user.id, ip_address=request.client.host if request.client else None)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 34 | `    return switch` | Devuelve el resultado de la función al código que la llamó. |
| 35 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 36 | `@router.get("/{switch_id}")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 37 | `def get_switch(switch_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):` | Declara la función `get_switch` con la lógica que se ejecutará cuando sea invocada. |
| 38 | `    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 39 | `    if not switch:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 40 | `        raise HTTPException(status_code=404, detail="Switch no encontrado")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 41 | `    return switch` | Devuelve el resultado de la función al código que la llamó. |
| 42 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 43 | `@router.put("/{switch_id}")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 44 | `def update_switch(switch_id: int, payload: SwitchUpdate, request: Request, db: Session = Depends(get_db), current_user=Depends(require_pe...` | Declara la función `update_switch` con la lógica que se ejecutará cuando sea invocada. |
| 45 | `    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 46 | `    if not switch:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 47 | `        raise HTTPException(status_code=404, detail="Switch no encontrado")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 48 | `    data = payload.dict(exclude_unset=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 49 | `    if "ssh_password" in data and data["ssh_password"]:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 50 | `        switch.ssh_password_encrypted = encrypt_value(data.pop("ssh_password"))` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 51 | `    elif "ssh_password" in data:` | Condición alternativa que se evalúa si la anterior no se cumple. |
| 52 | `        data.pop("ssh_password")` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 53 | `    for key, value in data.items():` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 54 | `        setattr(switch, key, value)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 55 | `    db.commit(); db.refresh(switch)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 56 | `    AuditService.log(db=db, action="UPDATE_SWITCH", entity_type="switch", entity_id=switch.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 57 | `                     detail=f"Se actualizó el switch {switch.name}", user_id=current_user.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 58 | `                     ip_address=request.client.host if request.client else None)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 59 | `    return switch` | Devuelve el resultado de la función al código que la llamó. |
| 60 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 61 | `@router.delete("/{switch_id}")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 62 | `def delete_switch(switch_id: int, request: Request, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.delete...` | Declara la función `delete_switch` con la lógica que se ejecutará cuando sea invocada. |
| 63 | `    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 64 | `    if not switch:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 65 | `        raise HTTPException(status_code=404, detail="Switch no encontrado")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 66 | `    switch.is_deleted = True` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 67 | `    db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 68 | `    AuditService.log(db=db, action="DELETE_SWITCH", entity_type="switch", entity_id=switch.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 69 | `                     detail=f"Se eliminó lógicamente el switch {switch.name}", user_id=current_user.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 70 | `                     ip_address=request.client.host if request.client else None)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 71 | `    return {"message": "Switch eliminado correctamente"}` | Devuelve el resultado de la función al código que la llamó. |
| 72 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 73 | `@router.post("/{switch_id}/test-ssh")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 74 | `def test_switch_ssh(switch_id: int, request: Request, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.test...` | Declara la función `test_switch_ssh` con la lógica que se ejecutará cuando sea invocada. |
| 75 | `    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 76 | `    if not switch:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 77 | `        raise HTTPException(status_code=404, detail="Switch no encontrado")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 78 | `    if not switch.ssh_password_encrypted:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 79 | `        raise HTTPException(status_code=400, detail="No hay contraseña SSH configurada")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 80 | `    ok = SSHService.test_connection(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 81 | `        host=switch.ip_address, port=switch.ssh_port, username=switch.ssh_username,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 82 | `        encrypted_password=switch.ssh_password_encrypted` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 83 | `    )` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 84 | `    switch.status = "online" if ok else "offline"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 85 | `    db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 86 | `    AuditService.log(db=db, action="TEST_SSH_SWITCH", entity_type="switch", entity_id=switch.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 87 | `                     detail=f"Prueba SSH: {'OK' if ok else 'ERROR'}", user_id=current_user.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 88 | `                     ip_address=request.client.host if request.client else None)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 89 | `    return {"connected": ok, "status": switch.status}` | Devuelve el resultado de la función al código que la llamó. |