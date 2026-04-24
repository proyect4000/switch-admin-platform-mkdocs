# backend/app/api/v1/auth.py

## Propósito

Archivo del proyecto ubicado en `backend/app/api/v1/auth.py`.

## Código fuente

```py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import verify_password, create_access_token, get_password_hash
from app.models.user import User
from app.schemas.auth import UserCreate
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/register")
def register_user(payload: UserCreate, db: Session = Depends(get_db)):
    exists = db.query(User).filter(
        (User.username == payload.username) | (User.email == payload.email)
    ).first()
    if exists:
        raise HTTPException(status_code=400, detail="Usuario o correo ya existe")
    user = User(
        username=payload.username,
        full_name=payload.full_name,
        email=payload.email,
        password_hash=get_password_hash(payload.password),
        role=payload.role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "Usuario creado correctamente", "id": user.id}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    token = create_access_token(subject=user.username)
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {"id": user.id, "username": user.username, "full_name": user.full_name, "role": user.role, "email": user.email}
    }

@router.get("/me")
def me(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "role": current_user.role,
    }
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from fastapi import APIRouter, Depends, HTTPException, status` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from fastapi.security import OAuth2PasswordRequestForm` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from app.core.database import get_db` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from app.core.security import verify_password, create_access_token, get_password_hash` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `from app.models.user import User` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 7 | `from app.schemas.auth import UserCreate` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `from app.dependencies import get_current_user` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 9 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 10 | `router = APIRouter()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 12 | `@router.post("/register")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 13 | `def register_user(payload: UserCreate, db: Session = Depends(get_db)):` | Declara la función `register_user` con la lógica que se ejecutará cuando sea invocada. |
| 14 | `    exists = db.query(User).filter(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `        (User.username == payload.username) \| (User.email == payload.email)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 16 | `    ).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 17 | `    if exists:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 18 | `        raise HTTPException(status_code=400, detail="Usuario o correo ya existe")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 19 | `    user = User(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `        username=payload.username,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `        full_name=payload.full_name,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `        email=payload.email,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `        password_hash=get_password_hash(payload.password),` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `        role=payload.role,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 25 | `    )` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 26 | `    db.add(user)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 27 | `    db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 28 | `    db.refresh(user)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 29 | `    return {"message": "Usuario creado correctamente", "id": user.id}` | Devuelve el resultado de la función al código que la llamó. |
| 30 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 31 | `@router.post("/login")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 32 | `def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):` | Declara la función `login` con la lógica que se ejecutará cuando sea invocada. |
| 33 | `    user = db.query(User).filter(User.username == form_data.username).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 34 | `    if not user or not verify_password(form_data.password, user.password_hash):` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 35 | `        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")` | Lanza una excepción para cortar el flujo y reportar un error controlado. |
| 36 | `    token = create_access_token(subject=user.username)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 37 | `    return {` | Devuelve el resultado de la función al código que la llamó. |
| 38 | `        "access_token": token,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 39 | `        "token_type": "bearer",` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 40 | `        "user": {"id": user.id, "username": user.username, "full_name": user.full_name, "role": user.role, "email": user.email}` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 41 | `    }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 42 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 43 | `@router.get("/me")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 44 | `def me(current_user=Depends(get_current_user)):` | Declara la función `me` con la lógica que se ejecutará cuando sea invocada. |
| 45 | `    return {` | Devuelve el resultado de la función al código que la llamó. |
| 46 | `        "id": current_user.id,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 47 | `        "username": current_user.username,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 48 | `        "full_name": current_user.full_name,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 49 | `        "email": current_user.email,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 50 | `        "role": current_user.role,` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 51 | `    }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |