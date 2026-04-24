# backend/create_admin.py

## Propósito

Archivo del proyecto ubicado en `backend/create_admin.py`.

## Código fuente

```py
from app.core.database import SessionLocal
from app.core.security import get_password_hash
from app.models.user import User

db = SessionLocal()

exists = db.query(User).filter(User.username == "admin").first()
if not exists:
    db.add(User(
        username="admin",
        full_name="Administrador General",
        email="admin@local.com",
        password_hash=get_password_hash("Admin123*"),
        role="superadmin",
        is_active=True
    ))
    db.commit()
    print("Administrador creado correctamente")
else:
    print("El usuario admin ya existe")

db.close()
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from app.core.database import SessionLocal` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from app.core.security import get_password_hash` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.models.user import User` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `db = SessionLocal()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 6 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 7 | `exists = db.query(User).filter(User.username == "admin").first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 8 | `if not exists:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 9 | `    db.add(User(` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 10 | `        username="admin",` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `        full_name="Administrador General",` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `        email="admin@local.com",` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `        password_hash=get_password_hash("Admin123*"),` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `        role="superadmin",` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `        is_active=True` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `    ))` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 17 | `    db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 18 | `    print("Administrador creado correctamente")` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 19 | `else:` | Bloque alternativo que se ejecuta cuando no se cumplen las condiciones previas. |
| 20 | `    print("El usuario admin ya existe")` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 21 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 22 | `db.close()` | Línea de implementación que forma parte del comportamiento interno del archivo. |