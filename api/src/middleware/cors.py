"""CORS middleware configuration."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..config import get_settings


def setup_cors(app: FastAPI) -> None:
    """Configure CORS middleware for the application."""
    settings = get_settings()

    # Build list of allowed origins
    allowed_origins = [settings.frontend_url]

    # Allow localhost for development
    if settings.is_development:
        allowed_origins.extend([
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ])

    # Use regex to match all Vercel deployments
    # This allows any *.vercel.app domain
    allow_origin_regex = r"https://.*\.vercel\.app"

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_origin_regex=allow_origin_regex,
        allow_credentials=True,  # Required for cookies
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=["*"],
        expose_headers=["*"],
    )
