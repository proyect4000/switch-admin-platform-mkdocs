from typing import Optional
from pydantic import BaseModel

class PortCreate(BaseModel):
    switch_id: int
    port_name: str
    port_number: Optional[int] = None
    description: Optional[str] = None
    admin_status: str = "down"
    oper_status: str = "down"
    speed: Optional[str] = None
    duplex: Optional[str] = None
    vlan: Optional[str] = None
    mac_address: Optional[str] = None
    connected_device_name: Optional[str] = None
    connected_device_ip: Optional[str] = None

class PortUpdate(BaseModel):
    port_name: Optional[str] = None
    port_number: Optional[int] = None
    description: Optional[str] = None
    admin_status: Optional[str] = None
    oper_status: Optional[str] = None
    speed: Optional[str] = None
    duplex: Optional[str] = None
    vlan: Optional[str] = None
    mac_address: Optional[str] = None
    connected_device_name: Optional[str] = None
    connected_device_ip: Optional[str] = None
