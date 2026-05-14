from typing import Optional
import time
from app.scrapers import get_scraper, ScraperResult
from app.core.anti_bot import exponential_backoff
from app.config import settings
from app.utils.logger import logger

class ScraperEngine:
    def __init__(self):
        self.timeout = settings.scraper_timeout
        self.retry_count = settings.scraper_retry_count
        self.delay = settings.scraper_delay
    
    def scrape_product(self, url: str) -> Optional[ScraperResult]:
        """Scrape product with retry logic and exponential backoff"""
        scraper = get_scraper(url)
        
        for attempt in range(self.retry_count):
            try:
                logger.info(f"Scraping {url} (attempt {attempt + 1}/{self.retry_count})")
                
                result = scraper.scrape()
                
                if result and result.name:
                    logger.info(f"Successfully scraped {url}: {result.name} - {result.price}")
                    return result
                
                logger.warning(f"Scraping returned incomplete data for {url}")
                
            except Exception as e:
                logger.error(f"Error scraping {url} on attempt {attempt + 1}: {e}")
            
            # Wait before retry with exponential backoff
            if attempt < self.retry_count - 1:
                delay = exponential_backoff(attempt, self.delay)
                logger.info(f"Waiting {delay:.2f}s before retry...")
                time.sleep(delay)
        
        logger.error(f"Failed to scrape {url} after {self.retry_count} attempts")
        return None

scraper_engine = ScraperEngine()
