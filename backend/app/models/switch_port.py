from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class SwitchPort(Base):
    __tablename__ = "switch_ports"

    id = Column(Integer, primary_key=True, index=True)
    switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)
    port_name = Column(String(50), nullable=False)
    port_number = Column(Integer, nullable=True)
    description = Column(String(200), nullable=True)
    admin_status = Column(String(20), default="down")
    oper_status = Column(String(20), default="down")
    speed = Column(String(30), nullable=True)
    duplex = Column(String(20), nullable=True)
    vlan = Column(String(30), nullable=True)
    mac_address = Column(String(50), nullable=True)
    connected_device_name = Column(String(150), nullable=True)
    connected_device_ip = Column(String(45), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
