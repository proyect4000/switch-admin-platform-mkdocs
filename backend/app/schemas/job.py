from typing import Optional
from pydantic import BaseModel

class JobCreate(BaseModel):
    job_name: str
    job_type: str
    cron_expression: str
    target_switch_id: Optional[int] = None
    is_active: bool = True
