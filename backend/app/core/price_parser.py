import re
from typing import Optional

def parse_price(price_text: str) -> Optional[float]:
    """Extract numeric price from text"""
    if not price_text:
        return None
    
    # Remove currency symbols and common text
    cleaned = re.sub(r'[^\d.,]', '', price_text)
    
    # Handle different decimal separators
    if ',' in cleaned and '.' in cleaned:
        # Determine which is decimal separator
        if cleaned.rindex(',') > cleaned.rindex('.'):
            cleaned = cleaned.replace('.', '').replace(',', '.')
        else:
            cleaned = cleaned.replace(',', '')
    elif ',' in cleaned:
        # Check if comma is decimal separator (European format)
        parts = cleaned.split(',')
        if len(parts) == 2 and len(parts[1]) == 2:
            cleaned = cleaned.replace(',', '.')
        else:
            cleaned = cleaned.replace(',', '')
    
    try:
        return float(cleaned)
    except ValueError:
        return None

def extract_currency(price_text: str) -> str:
    """Extract currency symbol from price text"""
    currency_map = {
        '$': 'USD',
        '€': 'EUR',
        '£': 'GBP',
        '₹': 'INR',
        'USD': 'USD',
        'EUR': 'EUR',
        'GBP': 'GBP',
        'INR': 'INR'
    }
    
    for symbol, code in currency_map.items():
        if symbol in price_text:
            return code
    
    return 'USD'
