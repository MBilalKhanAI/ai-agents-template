"""
Logging configuration for the XAgent application.
Sets up logging based on environment variables and provides a logger factory.
"""

import logging
import sys
from typing import Optional

from .config import settings

def setup_logging() -> None:
    """Set up logging configuration based on environment variables."""
    # Create a formatter
    formatter = logging.Formatter(settings.log_format)
    
    # Create a console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    # Get the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.log_level)
    root_logger.addHandler(console_handler)

def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Get a logger instance with the specified name.
    
    Args:
        name: The name of the logger. If None, returns the root logger.
        
    Returns:
        logging.Logger: A configured logger instance.
    """
    return logging.getLogger(name)

# Set up logging when the module is imported
setup_logging() 