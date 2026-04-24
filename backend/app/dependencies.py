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
        "report.export", "job.manage", "audit.read", "user.manage"
    },
    "admin": {
        "switch.create", "switch.update", "switch.test_ssh",
        "ssh.open_terminal", "discovery.run", "backup.run",
        "backup.download", "report.export", "audit.read", "user.manage"
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

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario inactivo"
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
