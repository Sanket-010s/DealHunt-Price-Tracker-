from typing import Optional
from app.scrapers.base import BaseScraper, ScraperResult
from app.core.price_parser import parse_price, extract_currency
from app.utils.logger import logger

class AmazonScraper(BaseScraper):
    def scrape(self) -> Optional[ScraperResult]:
        html = self.fetch_html()
        if not html:
            return None
        
        soup = self.parse_html(html)
        
        # Extract product name
        name = None
        name_selectors = ['#productTitle', 'span#productTitle', 'h1.product-title']
        for selector in name_selectors:
            element = soup.select_one(selector)
            if element:
                name = element.get_text(strip=True)
                break
        
        if not name:
            logger.warning(f"Could not extract name from {self.url}")
            return None
        
        # Extract price
        price = None
        price_selectors = [
            '.a-price .a-offscreen',
            'span.a-price-whole',
            '#priceblock_ourprice',
            '#priceblock_dealprice',
            '.a-price-range .a-offscreen'
        ]
        
        for selector in price_selectors:
            element = soup.select_one(selector)
            if element:
                price_text = element.get_text(strip=True)
                price = parse_price(price_text)
                if price:
                    break
        
        # Extract currency
        currency = "USD"
        price_element = soup.select_one('.a-price .a-offscreen')
        if price_element:
            currency = extract_currency(price_element.get_text())
        
        # Extract image
        image_url = None
        img_element = soup.select_one('#landingImage, #imgBlkFront')
        if img_element:
            image_url = img_element.get('src') or img_element.get('data-old-hires')
        
        return ScraperResult(name=name, price=price, currency=currency, image_url=image_url)
