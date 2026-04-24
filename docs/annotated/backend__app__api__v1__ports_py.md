# backend/app/api/v1/ports.py

## Propósito

Archivo del proyecto ubicado en `backend/app/api/v1/ports.py`.

## Código fuente

```py
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
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from fastapi import APIRouter, Depends, HTTPException` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import get_db` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from app.models.switch_port import SwitchPort` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from app.models.switch import Switch` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `from app.schemas.port import PortCreate, PortUpdate` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 7 | `from app.dependencies import get_current_user, require_permission` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 9 | `router = APIRouter()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 11 | `@router.get("/switch/{switch_id}")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 12 | `def list_ports_by_switch(switch_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):` | Declara la función `list_ports_by_switch` con la lógica que se ejecutará cuando sea invocada. |
| 13 | `    switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 14 | `    if not switch:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 15 | `        raise HTTPException(status_code=404, detail="Switch no encontrado")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 16 | `    return db.query(SwitchPort).filter(SwitchPort.switch_id == switch_id).order_by(SwitchPort.id.asc()).all()` | Devuelve el resultado de la función al código que la llamó. |
| 17 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 18 | `@router.post("/")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 19 | `def create_port(payload: PortCreate, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.update"))):` | Declara la función `create_port` con la lógica que se ejecutará cuando sea invocada. |
| 20 | `    port = SwitchPort(**payload.dict())` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `    db.add(port); db.commit(); db.refresh(port)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 22 | `    return port` | Devuelve el resultado de la función al código que la llamó. |
| 23 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 24 | `@router.put("/{port_id}")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 25 | `def update_port(port_id: int, payload: PortUpdate, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.update"...` | Declara la función `update_port` con la lógica que se ejecutará cuando sea invocada. |
| 26 | `    port = db.query(SwitchPort).filter(SwitchPort.id == port_id).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 27 | `    if not port:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 28 | `        raise HTTPException(status_code=404, detail="Puerto no encontrado")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 29 | `    data = payload.dict(exclude_unset=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 30 | `    for key, value in data.items():` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 31 | `        setattr(port, key, value)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 32 | `    db.commit(); db.refresh(port)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 33 | `    return port` | Devuelve el resultado de la función al código que la llamó. |
| 34 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 35 | `@router.delete("/{port_id}")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 36 | `def delete_port(port_id: int, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.delete"))):` | Declara la función `delete_port` con la lógica que se ejecutará cuando sea invocada. |
| 37 | `    port = db.query(SwitchPort).filter(SwitchPort.id == port_id).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 38 | `    if not port:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 39 | `        raise HTTPException(status_code=404, detail="Puerto no encontrado")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 40 | `    db.delete(port); db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 41 | `    return {"message": "Puerto eliminado correctamente"}` | Devuelve el resultado de la función al código que la llamó. |