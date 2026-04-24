from fastapi import APIRouter, Depends
from app.dependencies import get_current_user, require_permission, ROLE_PERMISSIONS

router = APIRouter()

ROLE_LABELS = {
    "superadmin": "Superadministrador",
    "admin": "Administrador de red",
    "operator": "Operador",
    "viewer": "Solo lectura",
}

@router.get("/")
def list_roles(current_user=Depends(get_current_user)):
    return [
        {
            "name": role,
            "label": ROLE_LABELS.get(role, role),
            "permissions": sorted(list(perms)),
        }
        for role, perms in ROLE_PERMISSIONS.items()
    ]

@router.get("/permissions")
def list_permissions(current_user=Depends(require_permission("user.manage"))):
    all_permissions = sorted({p for perms in ROLE_PERMISSIONS.values() for p in perms})
    return [{"code": p, "description": p.replace(".", " ").title()} for p in all_permissions]
