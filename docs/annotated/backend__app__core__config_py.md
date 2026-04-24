# backend/app/core/config.py

## Propósito

Archivo del proyecto ubicado en `backend/app/core/config.py`.

## Código fuente

```py
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Switch Admin Platform"
    API_V1_STR: str = "/api/v1"

    POSTGRES_SERVER: str = "db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "switchdb"

    SECRET_KEY: str = "change_me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    SSH_SECRET_KEY: str = "change_me_too"
    FRONTEND_ORIGIN: str = "http://localhost:5173"

    class Config:
        env_file = ".env"

settings = Settings()
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from pydantic import BaseSettings` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 3 | `class Settings(BaseSettings):` | Declara la clase `Settings` como unidad principal de este bloque. |
| 4 | `    APP_NAME: str = "Switch Admin Platform"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `    API_V1_STR: str = "/api/v1"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 6 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 7 | `    POSTGRES_SERVER: str = "db"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 8 | `    POSTGRES_USER: str = "postgres"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    POSTGRES_PASSWORD: str = "postgres"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    POSTGRES_DB: str = "switchdb"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 12 | `    SECRET_KEY: str = "change_me"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `    ALGORITHM: str = "HS256"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 16 | `    SSH_SECRET_KEY: str = "change_me_too"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `    FRONTEND_ORIGIN: str = "http://localhost:5173"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 18 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 19 | `    class Config:` | Declara la clase `Config` como unidad principal de este bloque. |
| 20 | `        env_file = ".env"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 22 | `settings = Settings()` | Asigna un valor a una variable o atributo para usarlo más adelante. |