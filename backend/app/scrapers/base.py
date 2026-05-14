from abc import ABC, abstractmethod
from typing import Optional, Dict
from bs4 import BeautifulSoup
import requests
from app.core.anti_bot import get_headers
from app.core.price_parser import parse_price, extract_currency
from app.utils.logger import logger

class ScraperResult:
    def __init__(self, name: str, price: Optional[float], currency: str = "USD", image_url: Optional[str] = None):
        self.name = name
        self.price = price
        self.currency = currency
        self.image_url = image_url

class BaseScraper(ABC):
    def __init__(self, url: str):
        self.url = url
    
    @abstractmethod
    def scrape(self) -> Optional[ScraperResult]:
        """Scrape product information from URL"""
        pass
    
    def fetch_html(self, timeout: int = 30) -> Optional[str]:
        """Fetch HTML content from URL"""
        try:
            response = requests.get(self.url, headers=get_headers(), timeout=timeout)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logger.error(f"Failed to fetch {self.url}: {e}")
            return None
    
    def parse_html(self, html: str) -> BeautifulSoup:
        """Parse HTML content"""
        return BeautifulSoup(html, 'html.parser')
