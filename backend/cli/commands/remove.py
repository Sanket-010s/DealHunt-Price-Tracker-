from app.db import crud
from cli.utils import get_db_session

def remove_product(product_id: int):
    """Remove a product from tracking"""
    db = get_db_session()
    
    try:
        product = crud.get_product(db, product_id)
        if not product:
            print(f"Error: Product with ID {product_id} not found")
            return
        
        name = product.name
        success = crud.delete_product(db, product_id)
        
        if success:
            print(f"✓ Product '{name}' removed successfully")
        else:
            print("Error: Failed to remove product")
    
    finally:
        db.close()
