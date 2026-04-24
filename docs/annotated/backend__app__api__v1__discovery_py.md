# backend/app/api/v1/discovery.py

## Propósito

Archivo del proyecto ubicado en `backend/app/api/v1/discovery.py`.

## Código fuente

```py
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
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from fastapi import APIRouter, Depends, HTTPException, Request` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import get_db` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from app.models.switch import Switch` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from app.models.device_neighbor import DeviceNeighbor` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `from app.models.discovery_run import DiscoveryRun` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 7 | `from app.dependencies import get_current_user, require_permission` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `from app.services.discovery_service import DiscoveryService` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 9 | `from app.services.audit_service import AuditService` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 10 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 11 | `router = APIRouter()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 13 | `@router.post("/switches/{switch_id}/run")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 14 | `def run_discovery(switch_id: int, request: Request, db: Session = Depends(get_db), current_user=Depends(require_permission("discovery.run...` | Declara la función `run_discovery` con la lógica que se ejecutará cuando sea invocada. |
| 15 | `    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 16 | `    if not switch:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 17 | `        raise HTTPException(status_code=404, detail="Switch no encontrado")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 18 | `    if not switch.ssh_password_encrypted:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 19 | `        raise HTTPException(status_code=400, detail="El switch no tiene credenciales SSH")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 20 | `    result = DiscoveryService.discover_switch(db=db, switch=switch, user_id=current_user.id)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `    AuditService.log(db=db, action="RUN_DISCOVERY", entity_type="switch", entity_id=switch.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `                     detail=result["summary"], user_id=current_user.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `                     ip_address=request.client.host if request.client else None)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `    return result` | Devuelve el resultado de la función al código que la llamó. |
| 25 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 26 | `@router.get("/switches/{switch_id}/neighbors")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 27 | `def get_neighbors(switch_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):` | Declara la función `get_neighbors` con la lógica que se ejecutará cuando sea invocada. |
| 28 | `    return db.query(DeviceNeighbor).filter(DeviceNeighbor.switch_id == switch_id).order_by(DeviceNeighbor.id.desc()).all()` | Devuelve el resultado de la función al código que la llamó. |
| 29 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 30 | `@router.get("/switches/{switch_id}/runs")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 31 | `def get_discovery_runs(switch_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):` | Declara la función `get_discovery_runs` con la lógica que se ejecutará cuando sea invocada. |
| 32 | `    return db.query(DiscoveryRun).filter(DiscoveryRun.switch_id == switch_id).order_by(DiscoveryRun.started_at.desc()).all()` | Devuelve el resultado de la función al código que la llamó. |