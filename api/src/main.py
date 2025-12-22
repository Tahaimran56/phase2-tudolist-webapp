"""FastAPI application entry point."""

from fastapi import FastAPI

from .api.auth import router as auth_router
from .api.tasks import router as tasks_router
from .config import get_settings
from .middleware.cors import setup_cors

settings = get_settings()

app = FastAPI(
    title="Todo Web App API",
    description="RESTful API for the Phase 2 Todo Web Application",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Setup CORS middleware
setup_cors(app)


@app.on_event("startup")
def initialize_database() -> None:
    """Initialize database tables on startup if they don't exist."""
    try:
        from .database import Base, engine
        from .models.task import Task
        from .models.user import User

        # Create all tables (this is idempotent - won't recreate existing tables)
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables initialized successfully")
    except Exception as e:
        print(f"⚠️  Database initialization warning: {e}")
        # Don't crash the app, just log the error
        import traceback
        traceback.print_exc()

# Include routers
app.include_router(auth_router)
app.include_router(tasks_router)


@app.get("/")
def root() -> dict[str, str]:
    """Root endpoint - health check."""
    return {"status": "healthy", "message": "Todo API is running"}


@app.get("/health")
def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}
