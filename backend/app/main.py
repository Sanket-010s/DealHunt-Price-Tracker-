from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.config import settings
from app.db.base import engine, Base
from app.api.v1 import api_router
from app.core.scheduler import price_scheduler
from app.utils.logger import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting Price Tracker API...")
    Base.metadata.create_all(bind=engine)
    price_scheduler.start()
    yield
    # Shutdown
    logger.info("Shutting down Price Tracker API...")
    price_scheduler.stop()

app = FastAPI(
    title="Price Tracker API",
    description="Track product prices and get alerts",
    version="1.0.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Price Tracker API", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.api_host, port=settings.api_port)
