from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas import SuccessResponse
from app.core.scheduler import price_scheduler

router = APIRouter()

@router.post("/check-all", response_model=SuccessResponse)
async def trigger_check_all(db: Session = Depends(get_db)):
    """Manually trigger price check for all products"""
    await price_scheduler.check_all_products()
    return SuccessResponse(success=True, message="Price check triggered for all products")

@router.get("/status")
def get_scheduler_status():
    """Get scheduler status"""
    return {
        "running": price_scheduler.scheduler.running,
        "interval_minutes": price_scheduler.interval_minutes
    }
