# Interview Prep Agent

An AI agent that analyses your résumé against a job description, generates personalised interview questions, evaluates your answers, and gives a readiness score.

## Requirements

- Docker + Docker Compose
- API keys for Groq and LangSmith

## Setup

```bash
git clone <your-repo>
cd interview-prep-agent
cp .env.example .env
# Add your API keys to .env
docker compose up --build
```

Then open http://localhost:8501 in your browser.

## Environment variables

```
GROQ_API_KEY=your_key_here
LANGSMITH_API_KEY=your_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=interview-prep-agent
```

## How it works

1. Upload your résumé PDF and paste the job description
2. The agent identifies skill gaps between your profile and the role
3. Answer 5 technical + 3 behavioural questions tailored to those gaps
4. Get scored feedback after each answer
5. Receive a final readiness score and improvement recommendations

## Stack

| Layer | Tech |
|---|---|
| Agent | LangGraph + Groq (llama-3.3-70b) |
| Memory | ChromaDB |
| Backend | FastAPI |
| Frontend | Streamlit |
| Observability | LangSmith |
| Infra | Docker Compose |

## Services

| Service | Port |
|---|---|
| Streamlit UI | 8501 |
| FastAPI backend | 8000 |
| ChromaDB | 8002 |