from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class DeviceLink(Base):
    __tablename__ = "device_links"

    id = Column(Integer, primary_key=True, index=True)
    source_switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)
    source_port_id = Column(Integer, ForeignKey("switch_ports.id", ondelete="SET NULL"), nullable=True)
    target_switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)
    target_port_id = Column(Integer, ForeignKey("switch_ports.id", ondelete="SET NULL"), nullable=True)
    link_type = Column(String(30), default="uplink")
    status = Column(String(20), default="active")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
