from app.db import crud
from cli.utils import get_db_session, format_table

def list_products(active_only: bool = False):
    """List all tracked products"""
    db = get_db_session()
    
    try:
        products = crud.get_products(db, active_only=active_only)
        
        if not products:
            print("No products found.")
            return
        
        headers = ["ID", "Name", "Current Price", "Currency", "Active", "Last Checked"]
        rows = []
        
        for p in products:
            price = f"{p.current_price:.2f}" if p.current_price else "N/A"
            last_checked = p.last_checked.strftime("%Y-%m-%d %H:%M") if p.last_checked else "Never"
            rows.append([
                p.id,
                p.name[:40],
                price,
                p.currency,
                "Yes" if p.is_active else "No",
                last_checked
            ])
        
        print(format_table(headers, rows))
        print(f"\nTotal: {len(products)} products")
        
    finally:
        db.close()
