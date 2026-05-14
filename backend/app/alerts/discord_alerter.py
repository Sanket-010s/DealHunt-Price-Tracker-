import httpx
from typing import Dict, Any
from app.alerts.base import BaseAlerter
from app.config import settings
from app.utils.logger import logger

class DiscordAlerter(BaseAlerter):
    def __init__(self):
        self.webhook_url = settings.discord_webhook_url
        self.enabled = settings.discord_enabled
    
    async def send_alert(self, message: str, metadata: Dict[str, Any] = None) -> bool:
        if not self.enabled or not self.webhook_url:
            logger.warning("Discord alerter is disabled or not configured")
            return False
        
        try:
            embed = self._create_embed(message, metadata)
            
            payload = {
                "content": "🔔 Price Alert!",
                "embeds": [embed]
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.post(self.webhook_url, json=payload)
                response.raise_for_status()
            
            logger.info("Discord alert sent successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send Discord alert: {e}")
            return False
    
    def _create_embed(self, message: str, metadata: Dict[str, Any] = None) -> Dict:
        metadata = metadata or {}
        
        embed = {
            "title": metadata.get('product_name', 'Price Alert'),
            "description": message,
            "color": 3066993,  # Green color
            "fields": []
        }
        
        if metadata.get('old_price'):
            embed["fields"].append({
                "name": "Old Price",
                "value": f"{metadata.get('currency', '$')}{metadata['old_price']:.2f}",
                "inline": True
            })
        
        if metadata.get('new_price'):
            embed["fields"].append({
                "name": "New Price",
                "value": f"{metadata.get('currency', '$')}{metadata['new_price']:.2f}",
                "inline": True
            })
        
        if metadata.get('product_url'):
            embed["url"] = metadata['product_url']
        
        if metadata.get('image_url'):
            embed["thumbnail"] = {"url": metadata['image_url']}
        
        return embed
