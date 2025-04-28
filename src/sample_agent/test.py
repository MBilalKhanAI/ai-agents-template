"""
Test script for the sample agent.

This script demonstrates how to use the agents directly without the API.
"""

import asyncio
from agents import Runner
from .agents import (
    triage_agent,
    analysis_agent,
    content_agent,
    safety_agent
)

async def test_agents():
    """Test all agents with sample inputs."""
    # Test analysis agent
    print("\nTesting Analysis Agent...")
    result = await Runner.run(
        analysis_agent,
        "Analyze the impact of AI on modern society"
    )
    print(f"Analysis Result: {result.final_output}")

    # Test content agent
    print("\nTesting Content Agent...")
    result = await Runner.run(
        content_agent,
        "Generate a blog post about renewable energy"
    )
    print(f"Content Result: {result.final_output}")

    # Test safety agent
    print("\nTesting Safety Agent...")
    result = await Runner.run(
        safety_agent,
        "Check if this content is safe: 'This is a test message'"
    )
    print(f"Safety Result: {result.final_output}")

    # Test triage agent
    print("\nTesting Triage Agent...")
    result = await Runner.run(
        triage_agent,
        "I need help analyzing market trends"
    )
    print(f"Triage Result: {result.final_output}")

if __name__ == "__main__":
    asyncio.run(test_agents()) 