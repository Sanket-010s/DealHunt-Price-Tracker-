#!/usr/bin/env python3
"""Seed database with sample data"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.db import SessionLocal, crud
from app.db.models import AlertType

def seed_data():
    """Add sample products and alerts"""
    db = SessionLocal()
    
    try:
        # Sample products
        samples = [
            {
                "url": "https://www.amazon.com/dp/B08N5WRWNW",
                "name": "Sample Product 1",
                "currency": "USD"
            },
            {
                "url": "https://www.flipkart.com/sample-product",
                "name": "Sample Product 2",
                "currency": "INR"
            }
        ]
        
        for sample in samples:
            existing = crud.get_product_by_url(db, sample["url"])
            if not existing:
                product = crud.create_product(db, **sample)
                print(f"Added: {product.name}")
                
                # Add sample alert
                crud.create_alert(
                    db,
                    product_id=product.id,
                    alert_type=AlertType.PERCENTAGE,
                    percentage_drop=10.0
                )
                print(f"  - Added 10% drop alert")
        
        print("\nSeed data added successfully!")
    
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
