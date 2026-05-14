from typing import Optional
from app.scrapers.base import BaseScraper, ScraperResult
from app.scrapers.amazon import AmazonScraper
from app.scrapers.flipkart import FlipkartScraper
from app.scrapers.bookdepository import BookDepositoryScraper
from app.scrapers.generic import GenericScraper
from app.utils.validators import extract_domain

def get_scraper(url: str) -> BaseScraper:
    """Factory function to get appropriate scraper based on URL"""
    domain = extract_domain(url)
    
    if 'amazon' in domain:
        return AmazonScraper(url)
    elif 'flipkart' in domain:
        return FlipkartScraper(url)
    elif 'bookdepository' in domain:
        return BookDepositoryScraper(url)
    else:
        return GenericScraper(url)

__all__ = [
    "BaseScraper",
    "ScraperResult",
    "AmazonScraper",
    "FlipkartScraper",
    "BookDepositoryScraper",
    "GenericScraper",
    "get_scraper"
]
