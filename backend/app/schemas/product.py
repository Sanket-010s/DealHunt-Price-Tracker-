from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    url: str
    name: str
    currency: str = "USD"

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    is_active: Optional[bool] = None

class PriceHistoryItem(BaseModel):
    price: float
    timestamp: datetime
    
    class Config:
        from_attributes = True

class Product(ProductBase):
    id: int
    current_price: Optional[float] = None
    image_url: Optional[str] = None
    is_active: bool
    last_checked: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class ProductWithHistory(Product):
    price_history: list[PriceHistoryItem] = []
