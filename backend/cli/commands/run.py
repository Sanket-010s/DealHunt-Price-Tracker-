import uvicorn
from app.config import settings

def run_server(host: str = None, port: int = None):
    """Run the FastAPI server"""
    host = host or settings.api_host
    port = port or settings.api_port
    
    print(f"Starting Price Tracker API on {host}:{port}")
    uvicorn.run("app.main:app", host=host, port=port, reload=True)
