from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.api.deps import get_db
from app.schemas import Alert, AlertCreate, SuccessResponse
from app.db import crud
from app.db.models import AlertType

router = APIRouter()

@router.get("/", response_model=List[Alert])
def get_alerts(product_id: Optional[int] = None, active_only: bool = True, db: Session = Depends(get_db)):
    """Get all alerts"""
    return crud.get_alerts(db, product_id=product_id, active_only=active_only)

@router.post("/", response_model=Alert, status_code=201)
def create_alert(alert: AlertCreate, db: Session = Depends(get_db)):
    """Create a new alert"""
    # Validate product exists
    product = crud.get_product(db, alert.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Validate alert parameters
    if alert.alert_type == AlertType.ABSOLUTE and alert.target_price is None:
        raise HTTPException(status_code=400, detail="target_price required for absolute alerts")
    
    if alert.alert_type == AlertType.PERCENTAGE and alert.percentage_drop is None:
        raise HTTPException(status_code=400, detail="percentage_drop required for percentage alerts")
    
    return crud.create_alert(
        db,
        product_id=alert.product_id,
        alert_type=alert.alert_type,
        target_price=alert.target_price,
        percentage_drop=alert.percentage_drop
    )

@router.delete("/{alert_id}", response_model=SuccessResponse)
def delete_alert(alert_id: int, db: Session = Depends(get_db)):
    """Delete an alert"""
    success = crud.delete_alert(db, alert_id)
    if not success:
        raise HTTPException(status_code=404, detail="Alert not found")
    return SuccessResponse(success=True, message="Alert deleted successfully")
