from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JobCreate(BaseModel):
    name: str
    payload: dict = {}
    priority: int = 1
    queue_id: int
    scheduled_at: Optional[datetime] = None


class JobResponse(BaseModel):
    id: int
    name: str
    payload: dict
    status: str
    priority: int
    retry_count: int
    queue_id: int

    class Config:
        from_attributes = True