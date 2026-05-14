from typing import Optional
from app.scrapers.base import BaseScraper, ScraperResult
from app.core.price_parser import parse_price, extract_currency
from app.utils.logger import logger

class FlipkartScraper(BaseScraper):
    def scrape(self) -> Optional[ScraperResult]:
        html = self.fetch_html()
        if not html:
            return None
        
        soup = self.parse_html(html)
        
        # Extract product name
        name = None
        name_selectors = [
            'span.B_NuCI',
            'h1.yhB1nd',
            'h1 span.B_NuCI'
        ]
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
            'div._30jeq3._16Jk6d',
            'div._30jeq3',
            'div._25b18c div._30jeq3'
        ]
        
        for selector in price_selectors:
            element = soup.select_one(selector)
            if element:
                price_text = element.get_text(strip=True)
                price = parse_price(price_text)
                if price:
                    break
        
        # Extract currency (Flipkart is primarily INR)
        currency = "INR"
        
        # Extract image
        image_url = None
        img_element = soup.select_one('img._396cs4, img._2r_T1I')
        if img_element:
            image_url = img_element.get('src')
        
        return ScraperResult(name=name, price=price, currency=currency, image_url=image_url)
