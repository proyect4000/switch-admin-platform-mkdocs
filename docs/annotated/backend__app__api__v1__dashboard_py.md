# backend/app/api/v1/dashboard.py

## Propósito

Archivo del proyecto ubicado en `backend/app/api/v1/dashboard.py`.

## Código fuente

```py
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
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from fastapi import APIRouter, Depends` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import get_db` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from app.models.switch import Switch` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from app.models.discovery_run import DiscoveryRun` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `from app.models.config_backup import ConfigBackup` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 7 | `from app.dependencies import get_current_user` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 9 | `router = APIRouter()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 11 | `@router.get("/summary")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 12 | `def get_dashboard_summary(db: Session = Depends(get_db), current_user=Depends(get_current_user)):` | Declara la función `get_dashboard_summary` con la lógica que se ejecutará cuando sea invocada. |
| 13 | `    total = db.query(Switch).filter(Switch.is_deleted == False).count()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 14 | `    online = db.query(Switch).filter(Switch.is_deleted == False, Switch.status == "online").count()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 15 | `    offline = db.query(Switch).filter(Switch.is_deleted == False, Switch.status == "offline").count()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 16 | `    discoveries_ok = db.query(DiscoveryRun).filter(DiscoveryRun.status == "success").count()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 17 | `    discoveries_error = db.query(DiscoveryRun).filter(DiscoveryRun.status == "error").count()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 18 | `    backups_total = db.query(ConfigBackup).count()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 19 | `    return {` | Devuelve el resultado de la función al código que la llamó. |
| 20 | `        "total_switches": total,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 21 | `        "online_switches": online,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 22 | `        "offline_switches": offline,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 23 | `        "discovery_success": discoveries_ok,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 24 | `        "discovery_error": discoveries_error,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 25 | `        "backups_total": backups_total` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 26 | `    }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |