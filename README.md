# Interview Prep Agent

An AI-powered interview preparation agent that reads your résumé and job description to generate personalised questions, evaluate your answers, and give you a final readiness score.

---

## The Problem

Most people prepare for interviews by reading generic questions from the internet. These questions are not tailored to their skills or the specific job they are applying for.

## What This Project Solves

You upload your **résumé** and paste a **job description** and the AI agent does everything else.

---

## How It Works

### Step 1 : Reads your résumé and job description
Extracts all text from your PDF résumé and the job posting.

### Step 2 : Finds your skill gaps
Compares what you have vs what the job needs. Shows you exactly what skills you are missing.

### Step 3 : Generates personalised questions
Creates 5 technical questions and 3 behavioural questions based specifically on your gaps : not generic ones.

### Step 4 : Evaluates your answers
You type your answer → AI scores it 1 to 10, tells you what was good, what was weak, and shows you a model answer.

### Step 5 : Tracks your progress
Stores every question and answer in a database so it can see how you improve across the session.

### Step 6 : Gives a final report
Shows your overall readiness score, your weakest areas, and 3 specific things to improve before the interview.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| FastAPI | Backend API |
| Streamlit | Web UI |
| LangGraph | AI agent flow control |
| Groq (llama-3.3-70b) | LLM inference |
| ChromaDB | Session memory and RAG |
| LangSmith | Tracing and observability |
| pdfplumber | PDF parsing |
| Docker Compose | Service orchestration |

---

## Setup
 
```bash
git clone https://github.com/YOUR_USERNAME/interview-prep-agent.git
cd interview-prep-agent
cp .env.example .env
# Add your API keys to .env
docker compose up
```
 
| Service | URL |
|---|---|
| Streamlit UI | http://localhost:8501 |
| FastAPI docs | http://localhost:8000/docs |
 
---
 
## API Endpoints
 
| Method | Endpoint | Description |
|---|---|---|
| POST | `/upload` | Upload résumé + job description |
| POST | `/analyse` | Run gap analysis |
| GET | `/questions/{session_id}` | Get questions |
| POST | `/evaluate` | Submit answer, get feedback |
| GET | `/report/{session_id}` | Get final report |
 
---
 
## Required ENV Variables
 
```
GROQ_API_KEY=
LANGSMITH_API_KEY=
LANGCHAIN_TRACING_V2=true
CHROMA_HOST=chromadb
CHROMA_PORT=8002
```