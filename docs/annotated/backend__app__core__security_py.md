# backend/app/core/security.py

## Propósito

Archivo del proyecto ubicado en `backend/app/core/security.py`.

## Código fuente

```py
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_access_token(token: str):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        return None
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from datetime import datetime, timedelta, timezone` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from jose import jwt, JWTError` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from passlib.context import CryptContext` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from app.core.config import settings` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 6 | `pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 8 | `def verify_password(plain_password: str, hashed_password: str) -> bool:` | Declara la función `verify_password` con la lógica que se ejecutará cuando sea invocada. |
| 9 | `    return pwd_context.verify(plain_password, hashed_password)` | Devuelve el resultado de la función al código que la llamó. |
| 10 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 11 | `def get_password_hash(password: str) -> str:` | Declara la función `get_password_hash` con la lógica que se ejecutará cuando sea invocada. |
| 12 | `    return pwd_context.hash(password)` | Devuelve el resultado de la función al código que la llamó. |
| 13 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 14 | `def create_access_token(subject: str) -> str:` | Declara la función `create_access_token` con la lógica que se ejecutará cuando sea invocada. |
| 15 | `    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `    payload = {"sub": subject, "exp": expire}` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)` | Devuelve el resultado de la función al código que la llamó. |
| 18 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 19 | `def decode_access_token(token: str):` | Declara la función `decode_access_token` con la lógica que se ejecutará cuando sea invocada. |
| 20 | `    try:` | Inicio del manejo controlado de errores para operaciones riesgosas. |
| 21 | `        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])` | Devuelve el resultado de la función al código que la llamó. |
| 22 | `    except JWTError:` | Captura una excepción específica para responder sin interrumpir toda la aplicación. |
| 23 | `        return None` | Devuelve el resultado de la función al código que la llamó. |