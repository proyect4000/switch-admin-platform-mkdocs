from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class SSHSession(Base):
    __tablename__ = "ssh_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    switch_id = Column(Integer, ForeignKey("switches.id"), nullable=False)
    session_uuid = Column(String(100), nullable=False, unique=True)
    client_ip = Column(String(64), nullable=True)
    started_at = Column(DateTime, server_default=func.now())
    ended_at = Column(DateTime, nullable=True)
    status = Column(String(20), nullable=False, default="open")
