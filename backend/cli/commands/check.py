import asyncio
from app.db import crud
from app.core.scheduler import price_scheduler
from cli.utils import get_db_session

def check_product(product_id: int = None):
    """Check price for a specific product or all products"""
    db = get_db_session()
    
    try:
        if product_id:
            product = crud.get_product(db, product_id)
            if not product:
                print(f"Error: Product with ID {product_id} not found")
                return
            
            print(f"Checking price for: {product.name}")
            asyncio.run(price_scheduler.check_product(db, product_id))
            
            db.refresh(product)
            if product.current_price:
                print(f"✓ Current price: {product.currency}{product.current_price:.2f}")
        else:
            print("Checking all products...")
            asyncio.run(price_scheduler.check_all_products())
            print("✓ Check completed")
    
    finally:
        db.close()
