# backend/app/core/crypto.py

## Propósito

Archivo del proyecto ubicado en `backend/app/core/crypto.py`.

## Código fuente

```py
import base64
import hashlib
from cryptography.fernet import Fernet
from app.core.config import settings

def _build_key(secret: str) -> bytes:
    digest = hashlib.sha256(secret.encode()).digest()
    return base64.urlsafe_b64encode(digest)

fernet = Fernet(_build_key(settings.SSH_SECRET_KEY))

def encrypt_value(value: str) -> str:
    return fernet.encrypt(value.encode()).decode()

def decrypt_value(value: str) -> str:
    return fernet.decrypt(value.encode()).decode()
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `import base64` | Importa un módulo o paquete necesario para este archivo. |
| 2 | `import hashlib` | Importa un módulo o paquete necesario para este archivo. |
| 3 | `from cryptography.fernet import Fernet` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from app.core.config import settings` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 6 | `def _build_key(secret: str) -> bytes:` | Declara la función `_build_key` con la lógica que se ejecutará cuando sea invocada. |
| 7 | `    digest = hashlib.sha256(secret.encode()).digest()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 8 | `    return base64.urlsafe_b64encode(digest)` | Devuelve el resultado de la función al código que la llamó. |
| 9 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 10 | `fernet = Fernet(_build_key(settings.SSH_SECRET_KEY))` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 12 | `def encrypt_value(value: str) -> str:` | Declara la función `encrypt_value` con la lógica que se ejecutará cuando sea invocada. |
| 13 | `    return fernet.encrypt(value.encode()).decode()` | Devuelve el resultado de la función al código que la llamó. |
| 14 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 15 | `def decrypt_value(value: str) -> str:` | Declara la función `decrypt_value` con la lógica que se ejecutará cuando sea invocada. |
| 16 | `    return fernet.decrypt(value.encode()).decode()` | Devuelve el resultado de la función al código que la llamó. |