from datetime import datetime
from typing import Optional

def format_price(price: Optional[float], currency: str = "USD") -> str:
    if price is None:
        return "N/A"
    symbols = {"USD": "$", "EUR": "€", "GBP": "£", "INR": "₹"}
    symbol = symbols.get(currency, currency)
    return f"{symbol}{price:.2f}"

def calculate_percentage_change(old_price: float, new_price: float) -> float:
    if old_price == 0:
        return 0.0
    return ((new_price - old_price) / old_price) * 100

def format_datetime(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")
