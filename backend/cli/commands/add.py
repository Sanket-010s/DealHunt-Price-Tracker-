import sys
from app.db import crud
from app.core.scraper import scraper_engine
from cli.utils import get_db_session

def add_product(url: str, name: str = None, currency: str = "USD"):
    """Add a new product to track"""
    db = get_db_session()
    
    try:
        # Check if exists
        existing = crud.get_product_by_url(db, url)
        if existing:
            print(f"Error: Product already exists (ID: {existing.id})")
            return
        
        # Scrape to get name if not provided
        if not name:
            print("Scraping product details...")
            result = scraper_engine.scrape_product(url)
            if result and result.name:
                name = result.name
                currency = result.currency
                print(f"Found: {name}")
            else:
                print("Error: Could not scrape product. Please provide name manually.")
                return
        
        # Create product
        product = crud.create_product(db, url, name, currency)
        print(f"✓ Product added successfully (ID: {product.id})")
        
        # Try to get initial price
        result = scraper_engine.scrape_product(url)
        if result and result.price:
            crud.update_product_price(db, product.id, result.price, result.image_url)
            crud.add_price_history(db, product.id, result.price)
            print(f"✓ Initial price: {currency}{result.price:.2f}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()
