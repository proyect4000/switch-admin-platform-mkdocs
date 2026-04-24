# backend/app/api/v1/history.py

## Propósito

Archivo del proyecto ubicado en `backend/app/api/v1/history.py`.

## Código fuente

```py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.ssh_session import SSHSession
from app.models.ssh_command import SSHCommand
from app.models.audit_log import AuditLog
from app.dependencies import require_permission

router = APIRouter()

@router.get("/sessions")
def list_ssh_sessions(db: Session = Depends(get_db), current_user=Depends(require_permission("audit.read"))):
    return db.query(SSHSession).order_by(SSHSession.started_at.desc()).all()

@router.get("/commands")
def list_ssh_commands(db: Session = Depends(get_db), current_user=Depends(require_permission("audit.read"))):
    return db.query(SSHCommand).order_by(SSHCommand.executed_at.desc()).all()

@router.get("/audit-logs")
def list_audit_logs(db: Session = Depends(get_db), current_user=Depends(require_permission("audit.read"))):
    return db.query(AuditLog).order_by(AuditLog.created_at.desc()).all()
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from fastapi import APIRouter, Depends` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import get_db` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from app.models.ssh_session import SSHSession` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from app.models.ssh_command import SSHCommand` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `from app.models.audit_log import AuditLog` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 7 | `from app.dependencies import require_permission` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 9 | `router = APIRouter()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 11 | `@router.get("/sessions")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 12 | `def list_ssh_sessions(db: Session = Depends(get_db), current_user=Depends(require_permission("audit.read"))):` | Declara la función `list_ssh_sessions` con la lógica que se ejecutará cuando sea invocada. |
| 13 | `    return db.query(SSHSession).order_by(SSHSession.started_at.desc()).all()` | Devuelve el resultado de la función al código que la llamó. |
| 14 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 15 | `@router.get("/commands")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 16 | `def list_ssh_commands(db: Session = Depends(get_db), current_user=Depends(require_permission("audit.read"))):` | Declara la función `list_ssh_commands` con la lógica que se ejecutará cuando sea invocada. |
| 17 | `    return db.query(SSHCommand).order_by(SSHCommand.executed_at.desc()).all()` | Devuelve el resultado de la función al código que la llamó. |
| 18 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 19 | `@router.get("/audit-logs")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 20 | `def list_audit_logs(db: Session = Depends(get_db), current_user=Depends(require_permission("audit.read"))):` | Declara la función `list_audit_logs` con la lógica que se ejecutará cuando sea invocada. |
| 21 | `    return db.query(AuditLog).order_by(AuditLog.created_at.desc()).all()` | Devuelve el resultado de la función al código que la llamó. |