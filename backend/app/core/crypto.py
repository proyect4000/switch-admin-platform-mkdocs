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
