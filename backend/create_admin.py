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
