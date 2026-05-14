from pydantic import BaseModel
from datetime import datetime
from app.db.models import NotificationChannel

class Notification(BaseModel):
    id: int
    alert_id: int
    channel: NotificationChannel
    message: str
    sent_at: datetime
    success: bool
    error_message: str | None = None
    
    class Config:
        from_attributes = True
