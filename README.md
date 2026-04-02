# llm-eval

![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0+-green.svg)

A Python library for evaluating LLM responses using Google Gemini as an automated judge.

## Overview

llm-eval provides a simple way to score LLM responses on five key dimensions: accuracy, relevance, coherence, hallucination risk, and conciseness. It uses Google's Gemini model to perform the evaluation and returns structured JSON results.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd llm-eval
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Setup

Create a `.env` file in the project root with your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

## Usage

### CLI

Use the command-line interface to evaluate responses:

```bash
python cli.py --question "What is the capital of France?" --response "Paris"
```

### API

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Send a POST request to `/evaluate`:

```bash
curl -X POST "http://localhost:8000/evaluate" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is the capital of France?", "response": "Paris"}'
```

## Example JSON Output

```json
{
  "accuracy": {
    "score": 10,
    "reason": "The response is factually correct."
  },
  "relevance": {
    "score": 10,
    "reason": "Directly answers the question."
  },
  "coherence": {
    "score": 9,
    "reason": "Clear and well-structured."
  },
  "hallucination_risk": {
    "score": 10,
    "reason": "No unsupported information."
  },
  "conciseness": {
    "score": 10,
    "reason": "Brief and to the point."
  }
}
```