"""
Agent definitions for the sample agent using OpenAI Agents SDK.

This module defines the agents used for different tasks with handoffs,
guardrails, and function tools.
"""

from typing import Dict, List, Optional, Any
from agents import Agent, InputGuardrail, GuardrailFunctionOutput, Runner, function_tool
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Output types
class AnalysisOutput(BaseModel):
    """Output model for analysis results."""
    insights: str
    recommendations: List[str]
    confidence: float

class ContentOutput(BaseModel):
    """Output model for content generation."""
    content: str
    sentiment: str
    safety_score: float

# Function tools
@function_tool
def analyze_sentiment(text: str) -> Dict[str, float]:
    """Analyze sentiment of text.
    
    Args:
        text: The text to analyze for sentiment
    """
    return {"sentiment_score": 0.8, "confidence": 0.95}

@function_tool
def check_content_safety(text: str) -> Dict[str, bool]:
    """Check if content is safe to post.
    
    Args:
        text: The content to check for safety
    """
    return {"is_safe": True, "risk_level": "low"}

@function_tool
def get_trending_topics() -> List[str]:
    """Get currently trending topics."""
    return ["AI", "Technology", "Innovation"]

# Guardrail function
async def content_guardrail(ctx, agent, input_data):
    """Guardrail to check content safety."""
    result = await Runner.run(safety_agent, input_data)
    final_output = result.final_output_as(ContentOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=final_output.safety_score < 0.5
    )

# Analysis Agent
analysis_agent = Agent(
    name="Analysis Agent",
    instructions="""You are an analysis expert. Your role is to:
    1. Analyze input data and generate insights
    2. Provide actionable recommendations
    3. Calculate confidence scores
    4. Consider historical context""",
    output_type=AnalysisOutput,
    tools=[analyze_sentiment, get_trending_topics]
)

# Content Agent
content_agent = Agent(
    name="Content Agent",
    instructions="""You are a content generation expert. Your role is to:
    1. Generate engaging content
    2. Analyze sentiment
    3. Ensure content safety
    4. Optimize for engagement""",
    output_type=ContentOutput,
    tools=[check_content_safety, analyze_sentiment],
    input_guardrails=[
        InputGuardrail(guardrail_function=content_guardrail)
    ]
)

# Safety Agent
safety_agent = Agent(
    name="Safety Agent",
    instructions="""You are a content safety expert. Your role is to:
    1. Check content for safety
    2. Score content risk
    3. Identify potential issues
    4. Provide safety recommendations""",
    output_type=ContentOutput,
    tools=[check_content_safety]
)

# Triage Agent
triage_agent = Agent(
    name="Triage Agent",
    instructions="""You are responsible for routing tasks to the appropriate specialist agent.
    Based on the input, determine whether it should be handled by:
    1. Analysis Agent - for data analysis and insights
    2. Content Agent - for content generation
    Provide clear reasoning for your routing decision.""",
    handoffs=[analysis_agent, content_agent]
)

# Set up handoffs between agents
content_agent.handoffs = [safety_agent]
safety_agent.handoffs = [analysis_agent]

__all__ = [
    'analysis_agent',
    'content_agent',
    'safety_agent',
    'triage_agent',
    'AnalysisOutput',
    'ContentOutput'
] 