# backend/app/api/v1/topology.py

## Propósito

Archivo del proyecto ubicado en `backend/app/api/v1/topology.py`.

## Código fuente

```py
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
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from fastapi import APIRouter, Depends, HTTPException` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import get_db` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from app.models.switch import Switch` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from app.models.device_link import DeviceLink` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `from app.models.switch_port import SwitchPort` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 7 | `from app.schemas.topology import LinkCreate, LinkUpdate` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `from app.dependencies import get_current_user, require_permission` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 9 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 10 | `router = APIRouter()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 12 | `@router.get("/")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 13 | `def get_topology(db: Session = Depends(get_db), current_user=Depends(get_current_user)):` | Declara la función `get_topology` con la lógica que se ejecutará cuando sea invocada. |
| 14 | `    switches = db.query(Switch).filter(Switch.is_deleted == False).all()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 15 | `    links = db.query(DeviceLink).all()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `    nodes, edges = [], []` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `    for sw in switches:` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 18 | `        nodes.append({` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 19 | `            "id": sw.id,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 20 | `            "label": f"{sw.name}\n{sw.ip_address}",` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 21 | `            "group": sw.status,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 22 | `            "shape": "box",` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 23 | `            "title": f"Marca: {sw.brand or '-'} \| Modelo: {sw.model or '-'} \| Ubicación: {sw.location or '-'}"` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 24 | `        })` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 25 | `    for link in links:` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 26 | `        source_port = db.query(SwitchPort).filter(SwitchPort.id == link.source_port_id).first() if link.source_port_id else None` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 27 | `        target_port = db.query(SwitchPort).filter(SwitchPort.id == link.target_port_id).first() if link.target_port_id else None` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 28 | `        edges.append({` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 29 | `            "id": link.id,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 30 | `            "from": link.source_switch_id,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 31 | `            "to": link.target_switch_id,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 32 | `            "label": f"{source_port.port_name if source_port else '?'} ↔ {target_port.port_name if target_port else '?'}",` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 33 | `            "status": link.status` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 34 | `        })` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 35 | `    return {"nodes": nodes, "edges": edges}` | Devuelve el resultado de la función al código que la llamó. |
| 36 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 37 | `@router.post("/links")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 38 | `def create_link(payload: LinkCreate, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.update"))):` | Declara la función `create_link` con la lógica que se ejecutará cuando sea invocada. |
| 39 | `    link = DeviceLink(**payload.dict())` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 40 | `    db.add(link); db.commit(); db.refresh(link)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 41 | `    return link` | Devuelve el resultado de la función al código que la llamó. |
| 42 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 43 | `@router.put("/links/{link_id}")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 44 | `def update_link(link_id: int, payload: LinkUpdate, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.update"...` | Declara la función `update_link` con la lógica que se ejecutará cuando sea invocada. |
| 45 | `    link = db.query(DeviceLink).filter(DeviceLink.id == link_id).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 46 | `    if not link:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 47 | `        raise HTTPException(status_code=404, detail="Enlace no encontrado")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 48 | `    data = payload.dict(exclude_unset=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 49 | `    for key, value in data.items():` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 50 | `        setattr(link, key, value)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 51 | `    db.commit(); db.refresh(link)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 52 | `    return link` | Devuelve el resultado de la función al código que la llamó. |
| 53 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 54 | `@router.delete("/links/{link_id}")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 55 | `def delete_link(link_id: int, db: Session = Depends(get_db), current_user=Depends(require_permission("switch.delete"))):` | Declara la función `delete_link` con la lógica que se ejecutará cuando sea invocada. |
| 56 | `    link = db.query(DeviceLink).filter(DeviceLink.id == link_id).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 57 | `    if not link:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 58 | `        raise HTTPException(status_code=404, detail="Enlace no encontrado")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 59 | `    db.delete(link); db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 60 | `    return {"message": "Enlace eliminado correctamente"}` | Devuelve el resultado de la función al código que la llamó. |