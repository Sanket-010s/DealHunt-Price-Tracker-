from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.db.models import AlertType

class AlertBase(BaseModel):
    alert_type: AlertType
    target_price: Optional[float] = None
    percentage_drop: Optional[float] = None

class AlertCreate(AlertBase):
    product_id: int

class Alert(AlertBase):
    id: int
    product_id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
