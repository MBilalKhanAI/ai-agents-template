"""
Sample Agent package.

This package provides a template for using OpenAI Agents SDK with FastAPI integration.
"""

import os
import uvicorn
from dotenv import load_dotenv
from .agents import (
    analysis_agent,
    content_agent,
    safety_agent,
    triage_agent,
    AnalysisOutput,
    ContentOutput
)
from .api import app

# Load environment variables
load_dotenv()

__version__ = "0.1.0"
__all__ = [
    'analysis_agent',
    'content_agent',
    'safety_agent',
    'triage_agent',
    'AnalysisOutput',
    'ContentOutput',
    'app'
]

def main() -> None:
    """Run the FastAPI application."""
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", "8000"))
    debug = os.getenv("DEBUG", "False").lower() == "true"
    
    uvicorn.run(
        "sample_agent.api:app",
        host=host,
        port=port,
        reload=debug
    )
