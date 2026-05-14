#!/usr/bin/env python3
"""Initialize the database"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.db.base import Base, engine
from app.utils.logger import logger

def init_db():
    """Create all database tables"""
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialized successfully!")

if __name__ == "__main__":
    init_db()
