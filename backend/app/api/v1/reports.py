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
