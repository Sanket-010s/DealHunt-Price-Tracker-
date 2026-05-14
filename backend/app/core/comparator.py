from typing import Optional
from app.db.models import Alert, AlertType
from app.utils.helpers import calculate_percentage_change

def should_trigger_alert(alert: Alert, old_price: Optional[float], new_price: float) -> bool:
    """Determine if an alert should be triggered based on price change"""
    
    if not alert.is_active:
        return False
    
    if alert.alert_type == AlertType.ABSOLUTE:
        if alert.target_price and new_price <= alert.target_price:
            return True
    
    elif alert.alert_type == AlertType.PERCENTAGE:
        if old_price and alert.percentage_drop:
            change = calculate_percentage_change(old_price, new_price)
            if change <= -abs(alert.percentage_drop):
                return True
    
    elif alert.alert_type == AlertType.ANY_DROP:
        if old_price and new_price < old_price:
            return True
    
    return False

def get_alert_message(alert: Alert, product_name: str, old_price: Optional[float], new_price: float, currency: str) -> str:
    """Generate alert message based on alert type"""
    
    if alert.alert_type == AlertType.ABSOLUTE:
        return f"Price Alert: {product_name} is now {currency}{new_price:.2f} (Target: {currency}{alert.target_price:.2f})"
    
    elif alert.alert_type == AlertType.PERCENTAGE:
        if old_price:
            change = calculate_percentage_change(old_price, new_price)
            return f"Price Drop Alert: {product_name} dropped {abs(change):.1f}% from {currency}{old_price:.2f} to {currency}{new_price:.2f}"
    
    elif alert.alert_type == AlertType.ANY_DROP:
        if old_price:
            return f"Price Drop: {product_name} decreased from {currency}{old_price:.2f} to {currency}{new_price:.2f}"
    
    return f"Price Alert: {product_name} is now {currency}{new_price:.2f}"
