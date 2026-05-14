from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.alerts.email_alerter import EmailAlerter
from app.alerts.discord_alerter import DiscordAlerter
from app.db.models import Alert, NotificationChannel
from app.db import crud
from app.utils.logger import logger

class AlertManager:
    def __init__(self):
        self.email_alerter = EmailAlerter()
        self.discord_alerter = DiscordAlerter()
    
    async def send_alerts(self, db: Session, alert: Alert, message: str, metadata: Dict[str, Any] = None):
        """Send alerts through all enabled channels"""
        
        # Send email
        if self.email_alerter.enabled:
            success = await self.email_alerter.send_alert(message, metadata)
            crud.create_notification(
                db=db,
                alert_id=alert.id,
                channel=NotificationChannel.EMAIL,
                message=message,
                success=success,
                error_message=None if success else "Failed to send email"
            )
        
        # Send Discord
        if self.discord_alerter.enabled:
            success = await self.discord_alerter.send_alert(message, metadata)
            crud.create_notification(
                db=db,
                alert_id=alert.id,
                channel=NotificationChannel.DISCORD,
                message=message,
                success=success,
                error_message=None if success else "Failed to send Discord message"
            )

alert_manager = AlertManager()
