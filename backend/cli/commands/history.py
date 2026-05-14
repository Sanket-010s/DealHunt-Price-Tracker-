from app.db import crud
from cli.utils import get_db_session, format_table

def show_history(product_id: int, days: int = 30):
    """Show price history for a product"""
    db = get_db_session()
    
    try:
        product = crud.get_product(db, product_id)
        if not product:
            print(f"Error: Product with ID {product_id} not found")
            return
        
        print(f"Price history for: {product.name}")
        print(f"Currency: {product.currency}\n")
        
        history = crud.get_price_history(db, product_id, days=days)
        
        if not history:
            print("No price history available.")
            return
        
        headers = ["Date", "Time", "Price"]
        rows = []
        
        for h in history:
            date = h.timestamp.strftime("%Y-%m-%d")
            time = h.timestamp.strftime("%H:%M:%S")
            rows.append([date, time, f"{h.price:.2f}"])
        
        print(format_table(headers, rows))
        print(f"\nTotal records: {len(history)}")
        
        if len(history) >= 2:
            first_price = history[0].price
            last_price = history[-1].price
            change = last_price - first_price
            change_pct = (change / first_price) * 100 if first_price > 0 else 0
            
            print(f"\nPrice change: {change:+.2f} ({change_pct:+.1f}%)")
    
    finally:
        db.close()
