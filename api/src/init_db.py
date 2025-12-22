"""Initialize database tables.

Run this script to create all database tables.
Usage: python api/src/init_db.py
"""

import sys
from pathlib import Path

# Add current directory to path so we can use absolute imports
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from database import Base, engine
from models.user import User
from models.task import Task

def init_db():
    """Create all database tables."""
    print("Creating database tables...")
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully!")
        print(f"Tables created: {list(Base.metadata.tables.keys())}")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    init_db()
