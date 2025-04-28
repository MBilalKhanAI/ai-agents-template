# Sample Agent with OpenAI Agents SDK

A template project demonstrating the use of OpenAI Agents SDK with FastAPI integration. This project showcases various features of the SDK including handoffs, guardrails, and function tools.

## Features

- Multiple specialized agents (Analysis, Content, Safety, Triage)
- Handoff capabilities between agents
- Content safety guardrails
- Function tools for sentiment analysis and safety checks
- FastAPI integration for easy API access
- Comprehensive error handling and logging

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -e .
```

3. Set up environment variables:
```bash
export OPENAI_API_KEY=your_api_key_here
```

## Running the API

Start the FastAPI server:
```bash
uvicorn sample_agent.api:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `POST /analyze`: Analyze content using the analysis agent
- `POST /generate`: Generate content using the content agent
- `POST /check-safety`: Check content safety using the safety agent
- `POST /triage`: Route request to appropriate agent using triage agent
- `GET /health`: Health check endpoint

## Example Usage

```python
import requests

# Analyze content
response = requests.post(
    "http://localhost:8000/analyze",
    json={
        "input_text": "Analyze this text for insights",
        "parameters": {}
    }
)
print(response.json())

# Generate content
response = requests.post(
    "http://localhost:8000/generate",
    json={
        "input_text": "Generate a blog post about AI",
        "parameters": {}
    }
)
print(response.json())
```

## Project Structure

```
sample_agent/
├── src/
│   └── sample_agent/
│       ├── __init__.py
│       ├── agents.py      # Agent definitions
│       └── api.py         # FastAPI application
├── pyproject.toml         # Project dependencies
└── README.md             # This file
```

## Contributing

Feel free to fork this repository and use it as a template for your own projects. The code is designed to be easily extensible and customizable.

## License

MIT License
