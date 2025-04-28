"""
Configuration management for the XAgent application.
Loads environment variables and provides typed configuration settings.
"""

import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings, Field

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # OpenAI API Configuration
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    
    # API Server Configuration
    api_host: str = Field("0.0.0.0", env="API_HOST")
    api_port: int = Field(8000, env="API_PORT")
    debug: bool = Field(False, env="DEBUG")
    
    # Logging Configuration
    log_level: str = Field("INFO", env="LOG_LEVEL")
    log_format: str = Field(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        env="LOG_FORMAT"
    )
    
    # Rate Limiting
    rate_limit_requests: int = Field(100, env="RATE_LIMIT_REQUESTS")
    rate_limit_period: int = Field(3600, env="RATE_LIMIT_PERIOD")
    
    # Analytics Configuration
    analytics_window_hours: int = Field(24, env="ANALYTICS_WINDOW_HOURS")
    analytics_threshold: float = Field(0.1, env="ANALYTICS_THRESHOLD")
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        case_sensitive = True

# Create a global settings instance
settings = Settings()

def get_settings() -> Settings:
    """Get the application settings.
    
    Returns:
        Settings: The application settings instance.
    """
    return settings 