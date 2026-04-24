# backend/app/api/v1/reports.py

## Propósito

Archivo del proyecto ubicado en `backend/app/api/v1/reports.py`.

## Código fuente

```py
import csv
import io
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.switch import Switch
from app.dependencies import require_permission

router = APIRouter()

@router.get("/switches.csv")
def export_switches_csv(db: Session = Depends(get_db), current_user=Depends(require_permission("report.export"))):
    rows = db.query(Switch).filter(Switch.is_deleted == False).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Nombre", "IP", "Marca", "Modelo", "Ubicación", "Estado"])
    for item in rows:
        writer.writerow([item.id, item.name, item.ip_address, item.brand, item.model, item.location, item.status])
    output.seek(0)
    return StreamingResponse(iter([output.getvalue()]), media_type="text/csv",
                             headers={"Content-Disposition": "attachment; filename=switches.csv"})
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `import csv` | Importa un módulo o paquete necesario para este archivo. |
| 2 | `import io` | Importa un módulo o paquete necesario para este archivo. |
| 3 | `from fastapi import APIRouter, Depends` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from fastapi.responses import StreamingResponse` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 7 | `from app.core.database import get_db` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `from app.models.switch import Switch` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 9 | `from app.dependencies import require_permission` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 10 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 11 | `router = APIRouter()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 13 | `@router.get("/switches.csv")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 14 | `def export_switches_csv(db: Session = Depends(get_db), current_user=Depends(require_permission("report.export"))):` | Declara la función `export_switches_csv` con la lógica que se ejecutará cuando sea invocada. |
| 15 | `    rows = db.query(Switch).filter(Switch.is_deleted == False).all()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 16 | `    output = io.StringIO()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `    writer = csv.writer(output)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 18 | `    writer.writerow(["ID", "Nombre", "IP", "Marca", "Modelo", "Ubicación", "Estado"])` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 19 | `    for item in rows:` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 20 | `        writer.writerow([item.id, item.name, item.ip_address, item.brand, item.model, item.location, item.status])` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 21 | `    output.seek(0)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 22 | `    return StreamingResponse(iter([output.getvalue()]), media_type="text/csv",` | Devuelve el resultado de la función al código que la llamó. |
| 23 | `                             headers={"Content-Disposition": "attachment; filename=switches.csv"})` | Asigna un valor a una variable o atributo para usarlo más adelante. |