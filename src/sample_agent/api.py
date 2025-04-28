"""
FastAPI application for the sample agent.

This module provides API endpoints to interact with the agents.
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, Dict, Any
from .agents import (
    triage_agent,
    analysis_agent,
    content_agent,
    safety_agent,
    AnalysisOutput,
    ContentOutput
)
from agents import Runner
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Sample Agent API",
    description="API for interacting with OpenAI Agents SDK sample agents",
    version="0.1.0"
)

class AgentRequest(BaseModel):
    """Request model for agent interactions."""
    input_text: str
    agent_type: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None

class AgentResponse(BaseModel):
    """Response model for agent interactions."""
    output: Dict[str, Any]
    agent_used: str
    processing_time: float
    status: str = "success"

@app.get("/")
async def root():
    """Root endpoint that redirects to docs."""
    return {"message": "Welcome to Sample Agent API. Visit /docs for API documentation."}

@app.get("/analyze")
async def analyze_content_get(text: str = Query(..., description="Text to analyze")):
    """Analyze content using the analysis agent (GET endpoint)."""
    try:
        start_time = time.time()
        result = await Runner.run(analysis_agent, text)
        return AgentResponse(
            output=result.final_output.dict(),
            agent_used="analysis_agent",
            processing_time=time.time() - start_time
        )
    except Exception as e:
        logger.error(f"Error in analyze_content: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze", response_model=AgentResponse)
async def analyze_content(request: AgentRequest):
    """Analyze content using the analysis agent (POST endpoint)."""
    try:
        start_time = time.time()
        result = await Runner.run(analysis_agent, request.input_text)
        return AgentResponse(
            output=result.final_output.dict(),
            agent_used="analysis_agent",
            processing_time=time.time() - start_time
        )
    except Exception as e:
        logger.error(f"Error in analyze_content: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/generate")
async def generate_content_get(text: str = Query(..., description="Prompt for content generation")):
    """Generate content using the content agent (GET endpoint)."""
    try:
        start_time = time.time()
        result = await Runner.run(content_agent, text)
        return AgentResponse(
            output=result.final_output.dict(),
            agent_used="content_agent",
            processing_time=time.time() - start_time
        )
    except Exception as e:
        logger.error(f"Error in generate_content: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate", response_model=AgentResponse)
async def generate_content(request: AgentRequest):
    """Generate content using the content agent (POST endpoint)."""
    try:
        start_time = time.time()
        result = await Runner.run(content_agent, request.input_text)
        return AgentResponse(
            output=result.final_output.dict(),
            agent_used="content_agent",
            processing_time=time.time() - start_time
        )
    except Exception as e:
        logger.error(f"Error in generate_content: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/check-safety")
async def check_safety_get(text: str = Query(..., description="Text to check for safety")):
    """Check content safety using the safety agent (GET endpoint)."""
    try:
        start_time = time.time()
        result = await Runner.run(safety_agent, text)
        return AgentResponse(
            output=result.final_output.dict(),
            agent_used="safety_agent",
            processing_time=time.time() - start_time
        )
    except Exception as e:
        logger.error(f"Error in check_safety: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/check-safety", response_model=AgentResponse)
async def check_safety(request: AgentRequest):
    """Check content safety using the safety agent (POST endpoint)."""
    try:
        start_time = time.time()
        result = await Runner.run(safety_agent, request.input_text)
        return AgentResponse(
            output=result.final_output.dict(),
            agent_used="safety_agent",
            processing_time=time.time() - start_time
        )
    except Exception as e:
        logger.error(f"Error in check_safety: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/triage")
async def triage_request_get(text: str = Query(..., description="Text to triage")):
    """Route request to appropriate agent using triage agent (GET endpoint)."""
    try:
        start_time = time.time()
        result = await Runner.run(triage_agent, text)
        return AgentResponse(
            output=result.final_output.dict(),
            agent_used="triage_agent",
            processing_time=time.time() - start_time
        )
    except Exception as e:
        logger.error(f"Error in triage_request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/triage", response_model=AgentResponse)
async def triage_request(request: AgentRequest):
    """Route request to appropriate agent using triage agent (POST endpoint)."""
    try:
        start_time = time.time()
        result = await Runner.run(triage_agent, request.input_text)
        return AgentResponse(
            output=result.final_output.dict(),
            agent_used="triage_agent",
            processing_time=time.time() - start_time
        )
    except Exception as e:
        logger.error(f"Error in triage_request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "version": "0.1.0"} 