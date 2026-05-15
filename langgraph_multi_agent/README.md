# LangGraph Multi-Agent Research System

## Features

- Web Search Agent
- Database Search Agent
- PDF Search Agent
- Parallel execution with LangGraph
- Result aggregation using LLM
- SQLite support
- PDF parsing support

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

## Setup Database

```bash
python setup_db.py
```

## Run the Application

```bash
python app.py
```

## Workflow

User Query
    ↓
Web Search
DB Search
PDF Search
    ↓
Combine Results
    ↓
Final Answer
