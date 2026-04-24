from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Switch(Base):
    __tablename__ = "switches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    hostname = Column(String(150), nullable=True)
    ip_address = Column(String(45), unique=True, nullable=False, index=True)
    brand = Column(String(80), nullable=True)
    model = Column(String(100), nullable=True)
    os_version = Column(String(100), nullable=True)
    ssh_port = Column(Integer, nullable=False, default=22)
    ssh_username = Column(String(100), nullable=False)
    ssh_auth_type = Column(String(20), nullable=False, default="password")
    ssh_password_encrypted = Column(String, nullable=True)
    ssh_private_key_encrypted = Column(String, nullable=True)
    location = Column(String(150), nullable=True)
    rack = Column(String(100), nullable=True)
    notes = Column(String, nullable=True)
    status = Column(String(20), nullable=False, default="unknown")
    is_deleted = Column(Boolean, nullable=False, default=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
