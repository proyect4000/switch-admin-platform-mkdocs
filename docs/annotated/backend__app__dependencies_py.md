# backend/app/dependencies.py

## Propósito

Archivo del proyecto ubicado en `backend/app/dependencies.py`.

## Código fuente

```py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import decode_access_token
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

ROLE_PERMISSIONS = {
    "superadmin": {
        "switch.create", "switch.update", "switch.delete", "switch.test_ssh",
        "ssh.open_terminal", "discovery.run", "backup.run", "backup.download",
        "report.export", "job.manage", "audit.read"
    },
    "admin": {
        "switch.create", "switch.update", "switch.test_ssh",
        "ssh.open_terminal", "discovery.run", "backup.run",
        "backup.download", "report.export", "audit.read"
    },
    "operator": {
        "switch.test_ssh", "ssh.open_terminal", "discovery.run", "backup.download"
    },
    "viewer": {
        "audit.read"
    }
}

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )

    username = payload.get("sub")
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado"
        )

    return user

def require_permission(permission_code: str):
    def checker(user=Depends(get_current_user)):
        permissions = ROLE_PERMISSIONS.get(user.role, set())
        if permission_code not in permissions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permiso insuficiente: {permission_code}"
            )
        return user
    return checker
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from fastapi import Depends, HTTPException, status` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from fastapi.security import OAuth2PasswordBearer` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `from app.core.database import get_db` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `from app.core.security import decode_access_token` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 7 | `from app.models.user import User` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 9 | `oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 11 | `ROLE_PERMISSIONS = {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    "superadmin": {` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 13 | `        "switch.create", "switch.update", "switch.delete", "switch.test_ssh",` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 14 | `        "ssh.open_terminal", "discovery.run", "backup.run", "backup.download",` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 15 | `        "report.export", "job.manage", "audit.read"` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 16 | `    },` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 17 | `    "admin": {` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 18 | `        "switch.create", "switch.update", "switch.test_ssh",` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 19 | `        "ssh.open_terminal", "discovery.run", "backup.run",` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 20 | `        "backup.download", "report.export", "audit.read"` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 21 | `    },` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 22 | `    "operator": {` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 23 | `        "switch.test_ssh", "ssh.open_terminal", "discovery.run", "backup.download"` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 24 | `    },` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 25 | `    "viewer": {` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 26 | `        "audit.read"` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 27 | `    }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 28 | `}` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 29 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 30 | `def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):` | Declara la función `get_current_user` con la lógica que se ejecutará cuando sea invocada. |
| 31 | `    payload = decode_access_token(token)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 32 | `    if not payload:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 33 | `        raise HTTPException(` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 34 | `            status_code=status.HTTP_401_UNAUTHORIZED,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 35 | `            detail="Token inválido o expirado"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 36 | `        )` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 37 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 38 | `    username = payload.get("sub")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 39 | `    user = db.query(User).filter(User.username == username).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 40 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 41 | `    if not user:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 42 | `        raise HTTPException(` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 43 | `            status_code=status.HTTP_401_UNAUTHORIZED,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 44 | `            detail="Usuario no encontrado"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 45 | `        )` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 46 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 47 | `    return user` | Devuelve el resultado de la función al código que la llamó. |
| 48 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 49 | `def require_permission(permission_code: str):` | Declara la función `require_permission` con la lógica que se ejecutará cuando sea invocada. |
| 50 | `    def checker(user=Depends(get_current_user)):` | Declara la función `checker` con la lógica que se ejecutará cuando sea invocada. |
| 51 | `        permissions = ROLE_PERMISSIONS.get(user.role, set())` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 52 | `        if permission_code not in permissions:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 53 | `            raise HTTPException(` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 54 | `                status_code=status.HTTP_403_FORBIDDEN,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 55 | `                detail=f"Permiso insuficiente: {permission_code}"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 56 | `            )` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 57 | `        return user` | Devuelve el resultado de la función al código que la llamó. |
| 58 | `    return checker` | Devuelve el resultado de la función al código que la llamó. |