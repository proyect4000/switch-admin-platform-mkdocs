from sqlalchemy import Column, Integer, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class SSHCommand(Base):
    __tablename__ = "ssh_commands"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("ssh_sessions.id", ondelete="CASCADE"), nullable=False)
    command_text = Column(Text, nullable=False)
    output_text = Column(Text, nullable=True)
    executed_at = Column(DateTime, server_default=func.now())
    success = Column(Boolean, default=True)
