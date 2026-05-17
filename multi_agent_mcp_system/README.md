
# Multi-Agent System with MCP and A2A using FastAPI

## Overview

This project demonstrates a production-style Multi-Agent AI System using:

- MCP (Model Context Protocol inspired architecture)
- A2A (Agent-to-Agent communication)
- FastAPI
- Streamlit
- OpenAI
- Real-world external APIs

The system includes:

- Weather MCP Server
- Finance MCP Server
- Media MCP Server
- World Data MCP Server
- Contextualist Agent
- Scout Agent
- Publisher Agent
- Streamlit UI

---

# Architecture

```text
User
  ↓
Streamlit UI
  ↓
Contextualist Agent
  ↓
Weather MCP
World Data MCP
  ↓
Scout Agent
  ↓
Finance MCP
Media MCP
  ↓
Publisher Agent
  ↓
AI Generated Article
```

---

# Project Structure

```text
multi_agent_mcp_system/
│
├── agents/
├── mcp_servers/
├── protocols/
├── ui/
├── shared/
├── requirements.txt
├── .env.example
└── README.md
```

---

# Features

## MCP Servers

### Weather MCP
- Current weather
- Humidity
- Temperature
- Wind speed

### Finance MCP
- Real stock prices
- Crypto lookup
- Market sentiment

### Media MCP
- Trending news
- Topic search

### World Data MCP
- Country information
- Population
- Capital
- Region

---

# Setup Instructions

## 1. Clone Project

```bash
unzip multi_agent_mcp_system.zip
cd multi_agent_mcp_system
```

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Rename:

```bash
.env.example → .env
```

Add your API keys.

---

# Required API Keys

| API | Purpose |
|---|---|
| OpenAI | Article generation |
| OpenWeatherMap | Weather |
| NewsAPI | News |
| Finnhub | Finance |

---

# Run MCP Servers

Open separate terminals.

## Weather MCP

```bash
uvicorn mcp_servers.weather_server:app --reload --port 8002
```

## Finance MCP

```bash
uvicorn mcp_servers.finance_server:app --reload --port 8003
```

## Media MCP

```bash
uvicorn mcp_servers.media_server:app --reload --port 8004
```

## World Data MCP

```bash
uvicorn mcp_servers.world_data_server:app --reload --port 8001
```

---

# Run Streamlit UI

```bash
streamlit run ui/app.py
```

---

# Example Workflow

1. User enters:
   - Country
   - City
   - Topic

2. Contextualist Agent:
   - Fetches country data
   - Fetches weather data

3. Scout Agent:
   - Fetches news
   - Fetches stock market data

4. Publisher Agent:
   - Uses OpenAI to generate article

5. Streamlit displays article

---

# MCP Communication

Agents communicate with MCP servers using FastAPI REST APIs.

Example:

```python
requests.get("http://localhost:8002/weather/London")
```

---

# Future Improvements

- Redis Pub/Sub
- Kafka
- LangGraph
- Vector databases
- Async orchestration
- Kubernetes deployment
- Authentication
- Observability

---

# Purpose of the Project

This project demonstrates:

- AI agent collaboration
- Modular MCP tool design
- Agent orchestration
- Real-time contextual data aggregation
- Autonomous AI workflows

It can evolve into:

- AI newsroom
- Research assistant
- Financial analyst platform
- Enterprise AI ecosystem
