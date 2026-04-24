from typing import Optional
from pydantic import BaseModel

class LinkCreate(BaseModel):
    source_switch_id: int
    source_port_id: Optional[int] = None
    target_switch_id: int
    target_port_id: Optional[int] = None
    link_type: str = "uplink"
    status: str = "active"

class LinkUpdate(BaseModel):
    source_port_id: Optional[int] = None
    target_port_id: Optional[int] = None
    link_type: Optional[str] = None
    status: Optional[str] = None
