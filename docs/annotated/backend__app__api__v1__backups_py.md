# backend/app/api/v1/backups.py

## Propósito

Archivo del proyecto ubicado en `backend/app/api/v1/backups.py`.

## Código fuente

```py
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
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from fastapi import APIRouter, Depends, HTTPException, Request` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import get_db` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from app.models.switch import Switch` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from app.models.config_backup import ConfigBackup` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `from app.dependencies import require_permission` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 7 | `from app.services.backup_service import BackupService` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `from app.services.audit_service import AuditService` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 9 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 10 | `router = APIRouter()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 12 | `@router.post("/switches/{switch_id}/run")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 13 | `def run_backup(switch_id: int, request: Request, backup_type: str = "running-config", db: Session = Depends(get_db), current_user=Depends...` | Declara la función `run_backup` con la lógica que se ejecutará cuando sea invocada. |
| 14 | `    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 15 | `    if not switch:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 16 | `        raise HTTPException(status_code=404, detail="Switch no encontrado")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 17 | `    backup = BackupService.run_backup(db, switch, backup_type, current_user.id)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 18 | `    AuditService.log(db=db, action="RUN_BACKUP", entity_type="switch", entity_id=switch.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 19 | `                     detail=f"Backup generado: {backup.filename}", user_id=current_user.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `                     ip_address=request.client.host if request.client else None)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `    return backup` | Devuelve el resultado de la función al código que la llamó. |
| 22 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 23 | `@router.get("/switches/{switch_id}")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 24 | `def list_backups(switch_id: int, db: Session = Depends(get_db), current_user=Depends(require_permission("backup.download"))):` | Declara la función `list_backups` con la lógica que se ejecutará cuando sea invocada. |
| 25 | `    return db.query(ConfigBackup).filter(ConfigBackup.switch_id == switch_id).order_by(ConfigBackup.created_at.desc()).all()` | Devuelve el resultado de la función al código que la llamó. |
| 26 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 27 | `@router.get("/{backup_id}")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 28 | `def get_backup(backup_id: int, db: Session = Depends(get_db), current_user=Depends(require_permission("backup.download"))):` | Declara la función `get_backup` con la lógica que se ejecutará cuando sea invocada. |
| 29 | `    backup = db.query(ConfigBackup).filter(ConfigBackup.id == backup_id).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 30 | `    if not backup:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 31 | `        raise HTTPException(status_code=404, detail="Backup no encontrado")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 32 | `    return backup` | Devuelve el resultado de la función al código que la llamó. |