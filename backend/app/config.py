from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Database
    database_url: str = "sqlite:///./data/tracker.db"
    
    # Scraper
    scraper_timeout: int = 30
    scraper_retry_count: int = 3
    scraper_delay: int = 2
    use_playwright: bool = False
    
    # Scheduler
    scheduler_interval_minutes: int = 60
    
    # Email
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_password: str = ""
    smtp_from: str = ""
    email_enabled: bool = True
    
    # Discord
    discord_webhook_url: str = ""
    discord_enabled: bool = True
    
    # Proxy
    proxy_enabled: bool = False
    proxy_list_file: str = "./data/proxies.txt"
    
    # Logging
    log_level: str = "INFO"
    log_file: str = "./data/logs/tracker.log"
    
    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    cors_origins: str = "http://localhost:5173,http://localhost:3000"
    
    @property
    def cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
