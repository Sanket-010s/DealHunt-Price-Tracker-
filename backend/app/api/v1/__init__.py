from fastapi import APIRouter
from app.api.v1 import products, alerts, notifications, jobs, health

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(alerts.router, prefix="/alerts", tags=["alerts"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
