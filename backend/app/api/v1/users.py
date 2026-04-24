from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_password_hash
from app.dependencies import get_current_user, require_permission, ROLE_PERMISSIONS
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

router = APIRouter()

@router.get("/")
def list_users(db: Session = Depends(get_db), current_user=Depends(require_permission("user.manage"))):
    users = db.query(User).order_by(User.id.desc()).all()
    return [
        {
            "id": u.id,
            "username": u.username,
            "full_name": u.full_name,
            "email": u.email,
            "role": u.role,
            "is_active": u.is_active,
            "created_at": u.created_at,
        }
        for u in users
    ]

@router.post("/")
def create_user(payload: UserCreate, db: Session = Depends(get_db), current_user=Depends(require_permission("user.manage"))):
    exists = db.query(User).filter((User.username == payload.username) | (User.email == payload.email)).first()
    if exists:
        raise HTTPException(status_code=400, detail="Usuario o correo ya existe")
    if payload.role not in ROLE_PERMISSIONS:
        raise HTTPException(status_code=400, detail="Rol no válido")
    user = User(
        username=payload.username,
        full_name=payload.full_name,
        email=payload.email,
        password_hash=get_password_hash(payload.password),
        role=payload.role,
        is_active=payload.is_active,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "Usuario creado correctamente", "id": user.id}

@router.put("/{user_id}")
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db), current_user=Depends(require_permission("user.manage"))):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    data = payload.dict(exclude_unset=True)
    if "role" in data and data["role"] not in ROLE_PERMISSIONS:
        raise HTTPException(status_code=400, detail="Rol no válido")
    if data.get("password"):
        user.password_hash = get_password_hash(data.pop("password"))
    elif "password" in data:
        data.pop("password")
    for key, value in data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return {"message": "Usuario actualizado correctamente", "id": user.id}

@router.delete("/{user_id}")
def disable_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(require_permission("user.manage"))):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    user.is_active = False
    db.commit()
    return {"message": "Usuario desactivado correctamente"}
