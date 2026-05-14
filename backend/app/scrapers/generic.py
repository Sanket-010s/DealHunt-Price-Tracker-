from typing import Optional
from app.scrapers.base import BaseScraper, ScraperResult
from app.core.price_parser import parse_price, extract_currency
from app.utils.logger import logger

class GenericScraper(BaseScraper):
    def scrape(self) -> Optional[ScraperResult]:
        html = self.fetch_html()
        if not html:
            return None
        
        soup = self.parse_html(html)
        
        # Try common name selectors
        name = None
        name_selectors = [
            'h1[itemprop="name"]',
            'h1.product-title',
            'h1.product-name',
            'h1',
            '[itemprop="name"]',
            'meta[property="og:title"]'
        ]
        
        for selector in name_selectors:
            element = soup.select_one(selector)
            if element:
                if element.name == 'meta':
                    name = element.get('content', '').strip()
                else:
                    name = element.get_text(strip=True)
                if name:
                    break
        
        if not name:
            logger.warning(f"Could not extract name from {self.url}")
            return None
        
        # Try common price selectors
        price = None
        price_selectors = [
            '[itemprop="price"]',
            '.price',
            '.product-price',
            'span.price',
            'div.price',
            'meta[property="og:price:amount"]'
        ]
        
        for selector in price_selectors:
            element = soup.select_one(selector)
            if element:
                if element.name == 'meta':
                    price_text = element.get('content', '')
                else:
                    price_text = element.get_text(strip=True)
                price = parse_price(price_text)
                if price:
                    break
        
        # Extract currency
        currency = "USD"
        currency_element = soup.select_one('[itemprop="priceCurrency"], meta[property="og:price:currency"]')
        if currency_element:
            if currency_element.name == 'meta':
                currency = currency_element.get('content', 'USD')
            else:
                currency = currency_element.get_text(strip=True) or "USD"
        
        # Try common image selectors
        image_url = None
        img_selectors = [
            'img[itemprop="image"]',
            'img.product-image',
            'meta[property="og:image"]'
        ]
        
        for selector in img_selectors:
            element = soup.select_one(selector)
            if element:
                if element.name == 'meta':
                    image_url = element.get('content')
                else:
                    image_url = element.get('src')
                if image_url:
                    break
        
        return ScraperResult(name=name, price=price, currency=currency, image_url=image_url)
