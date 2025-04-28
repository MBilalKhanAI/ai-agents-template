# Sample Agent

A sample agent implementation using OpenAI Agents SDK, featuring multiple specialized agents for content creation, social media management, analytics, and engagement.

## Features

- **Content Creator Agent**: Generates engaging content for social media platforms
- **Social Media Manager Agent**: Manages and schedules social media posts
- **Analytics Agent**: Analyzes social media metrics and generates insights
- **Engagement Agent**: Monitors and responds to social media interactions
- **FastAPI Integration**: RESTful API endpoints for agent interactions
- **Environment Configuration**: Easy configuration through `.env` file
- **Development Tools**: Includes testing and code quality tools

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sample_agent.git
cd sample_agent
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the package in development mode:
```bash
pip install -e .
```

4. Create a `.env` file with your configuration:
```env
OPENAI_API_KEY=your_api_key_here
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True
```

## Usage

### Running the API Server

```bash
python -m sample_agent
```

The server will start at `http://localhost:8000`. You can access the API documentation at `http://localhost:8000/docs`.

### API Endpoints

- `POST /api/content/create`: Generate content
- `POST /api/social/schedule`: Schedule social media posts
- `POST /api/analytics/analyze`: Analyze social media metrics
- `POST /api/engagement/monitor`: Monitor social media engagement
- `GET /health`: Health check endpoint

### Example API Usage

```python
import requests

# Generate content
response = requests.post(
    "http://localhost:8000/api/content/create",
    json={
        "topic": "AI in Healthcare",
        "platform": "twitter",
        "tone": "professional"
    }
)
print(response.json())

# Analyze metrics
response = requests.post(
    "http://localhost:8000/api/analytics/analyze",
    json={
        "platform": "twitter",
        "metrics": ["engagement", "reach", "impressions"]
    }
)
print(response.json())
```

## Development

### Running Tests

```bash
pytest
```

### Code Quality

```bash
# Format code
black .

# Sort imports
isort .

# Lint code
flake8
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
