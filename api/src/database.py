"""SQLAlchemy database configuration and session management."""

from collections.abc import Generator
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from .config import get_settings


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""

    pass


settings = get_settings()

# Create database engine with connection pooling
# Convert postgresql:// to postgresql+psycopg2:// if needed for Vercel compatibility
db_url = settings.database_url
if db_url.startswith("postgresql://"):
    db_url = db_url.replace("postgresql://", "postgresql+psycopg2://", 1)

# For serverless (Vercel), use minimal connection pooling
engine = create_engine(
    db_url,
    pool_pre_ping=True,  # Verify connections before use
    pool_size=2,  # Smaller pool for serverless
    max_overflow=5,  # Reduced overflow
    pool_recycle=300,  # Recycle connections after 5 minutes
    echo=settings.is_development,  # Log SQL in development
    connect_args={
        "connect_timeout": 10,
    }  # Remove sslmode here - it's already in the URL
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, Any, None]:
    """Dependency to get database session.

    Yields a database session and ensures it's closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
