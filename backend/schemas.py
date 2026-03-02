from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User_Event(BaseModel):
    object_detect: str
    confidence: float
    camera_id: Optional[int] = None
    is_alert: bool

class EventResponse(BaseModel):
    id: int
    object_detect: str
    confidence: float
    camera_id: Optional[int] = None
    created_at: datetime
    is_alert: bool

    class Config:
        from_attributes = True
    