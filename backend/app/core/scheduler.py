from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from sqlalchemy.orm import Session
from app.db import SessionLocal, crud
from app.core.scraper import scraper_engine
from app.core.comparator import should_trigger_alert, get_alert_message
from app.alerts.alert_manager import alert_manager
from app.config import settings
from app.utils.logger import logger

class PriceScheduler:
    def __init__(self):
        self.scheduler = AsyncIOScheduler()
        self.interval_minutes = settings.scheduler_interval_minutes
    
    async def check_all_products(self):
        """Check prices for all active products"""
        logger.info("Starting scheduled price check...")
        
        db: Session = SessionLocal()
        try:
            products = crud.get_products(db, active_only=True)
            logger.info(f"Checking {len(products)} active products")
            
            for product in products:
                await self.check_product(db, product.id)
            
            logger.info("Scheduled price check completed")
        except Exception as e:
            logger.error(f"Error in scheduled check: {e}")
        finally:
            db.close()
    
    async def check_product(self, db: Session, product_id: int):
        """Check price for a single product"""
        try:
            product = crud.get_product(db, product_id)
            if not product or not product.is_active:
                return
            
            logger.info(f"Checking price for: {product.name}")
            
            # Scrape current price
            result = scraper_engine.scrape_product(product.url)
            if not result or result.price is None:
                logger.warning(f"Failed to get price for {product.name}")
                return
            
            old_price = product.current_price
            new_price = result.price
            
            # Update product
            crud.update_product_price(db, product_id, new_price, result.image_url)
            
            # Add to price history
            crud.add_price_history(db, product_id, new_price)
            
            # Check alerts
            alerts = crud.get_alerts(db, product_id=product_id, active_only=True)
            
            for alert in alerts:
                if should_trigger_alert(alert, old_price, new_price):
                    message = get_alert_message(alert, product.name, old_price, new_price, product.currency)
                    
                    metadata = {
                        'product_name': product.name,
                        'product_url': product.url,
                        'old_price': old_price,
                        'new_price': new_price,
                        'currency': product.currency,
                        'image_url': product.image_url,
                        'subject': f'Price Alert: {product.name}'
                    }
                    
                    await alert_manager.send_alerts(db, alert, message, metadata)
                    logger.info(f"Alert triggered for {product.name}")
        
        except Exception as e:
            logger.error(f"Error checking product {product_id}: {e}")
    
    def start(self):
        """Start the scheduler"""
        self.scheduler.add_job(
            self.check_all_products,
            trigger=IntervalTrigger(minutes=self.interval_minutes),
            id='price_check',
            name='Check product prices',
            replace_existing=True
        )
        self.scheduler.start()
        logger.info(f"Scheduler started (interval: {self.interval_minutes} minutes)")
    
    def stop(self):
        """Stop the scheduler"""
        self.scheduler.shutdown()
        logger.info("Scheduler stopped")

price_scheduler = PriceScheduler()
