from typing import Optional
from app.scrapers.base import BaseScraper, ScraperResult
from app.core.price_parser import parse_price, extract_currency
from app.utils.logger import logger

class BookDepositoryScraper(BaseScraper):
    def scrape(self) -> Optional[ScraperResult]:
        html = self.fetch_html()
        if not html:
            return None
        
        soup = self.parse_html(html)
        
        # Extract product name
        name = None
        name_element = soup.select_one('h1[itemprop="name"]')
        if name_element:
            name = name_element.get_text(strip=True)
        
        if not name:
            logger.warning(f"Could not extract name from {self.url}")
            return None
        
        # Extract price
        price = None
        price_element = soup.select_one('span.sale-price, span[itemprop="price"]')
        if price_element:
            price_text = price_element.get_text(strip=True)
            price = parse_price(price_text)
        
        # Extract currency
        currency = "USD"
        if price_element:
            currency = extract_currency(price_element.get_text())
        
        # Extract image
        image_url = None
        img_element = soup.select_one('img.book-img')
        if img_element:
            image_url = img_element.get('src')
        
        return ScraperResult(name=name, price=price, currency=currency, image_url=image_url)
