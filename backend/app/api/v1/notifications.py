from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.schemas import Notification
from app.db import crud

router = APIRouter()

@router.get("/", response_model=List[Notification])
def get_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get notification history"""
    return crud.get_notifications(db, skip=skip, limit=limit)
