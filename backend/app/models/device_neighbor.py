from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class DeviceNeighbor(Base):
    __tablename__ = "device_neighbors"

    id = Column(Integer, primary_key=True, index=True)
    switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)
    local_port = Column(String(100), nullable=False)
    neighbor_name = Column(String(150), nullable=True)
    neighbor_ip = Column(String(45), nullable=True)
    neighbor_platform = Column(String(150), nullable=True)
    neighbor_port = Column(String(100), nullable=True)
    protocol = Column(String(20), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
