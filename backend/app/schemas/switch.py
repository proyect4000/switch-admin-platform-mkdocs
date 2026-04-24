from typing import Optional
from pydantic import BaseModel, IPvAnyAddress

class SwitchCreate(BaseModel):
    name: str
    hostname: Optional[str] = None
    ip_address: IPvAnyAddress
    brand: Optional[str] = None
    model: Optional[str] = None
    os_version: Optional[str] = None
    ssh_port: int = 22
    ssh_username: str
    ssh_password: Optional[str] = None
    ssh_auth_type: str = "password"
    location: Optional[str] = None
    rack: Optional[str] = None
    notes: Optional[str] = None

class SwitchUpdate(BaseModel):
    name: Optional[str] = None
    hostname: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    os_version: Optional[str] = None
    ssh_port: Optional[int] = None
    ssh_username: Optional[str] = None
    ssh_password: Optional[str] = None
    ssh_auth_type: Optional[str] = None
    location: Optional[str] = None
    rack: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[str] = None
