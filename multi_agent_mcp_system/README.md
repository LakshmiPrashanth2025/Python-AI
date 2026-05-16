
# Multi-Agent System with MCP and A2A using FastAPI

## Overview

This project demonstrates a production-inspired Multi-Agent AI System using:

* MCP (Model Context Protocol inspired architecture)
* A2A (Agent-to-Agent communication)
* FastAPI microservices
* Streamlit UI
* OpenAI LLM integration
* Real-world APIs for weather, finance, media, and world data

The application simulates how multiple AI agents collaborate using contextual tools exposed through MCP servers.

---

# Project Goals

This project is designed to demonstrate:

* AI agent orchestration
* Modular MCP tool architecture
* Agent-to-Agent collaboration
* Real-time contextual data aggregation
* Distributed AI systems
* FastAPI microservice communication
* LLM-powered article generation
* Scalable enterprise AI patterns

---

# System Architecture

```text
                         ┌────────────────────┐
                         │    Streamlit UI    │
                         └─────────┬──────────┘
                                   │
                                   ▼
                     ┌────────────────────────┐
                     │ Contextualist Agent    │
                     └─────────┬──────────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
      ┌─────────────────┐          ┌─────────────────┐
      │ World Data MCP  │          │ Weather MCP     │
      └─────────────────┘          └─────────────────┘

                                   ▼
                     ┌────────────────────────┐
                     │ Scout Agent            │
                     └─────────┬──────────────┘
                               │
             ┌─────────────────┴─────────────────┐
             │                                   │
             ▼                                   ▼
   ┌─────────────────┐                 ┌─────────────────┐
   │ Finance MCP     │                 │ Media MCP       │
   └─────────────────┘                 └─────────────────┘

                                   ▼
                     ┌────────────────────────┐
                     │ Publisher Agent        │
                     └─────────┬──────────────┘
                               │
                               ▼
                     ┌────────────────────────┐
                     │ AI Generated Article   │
                     └────────────────────────┘
```

---

# Project Structure

```text
multi_agent_mcp_system/
│
├── agents/
│   ├── contextualist_agent.py
│   ├── scout_agent.py
│   └── publisher_agent.py
│
├── mcp_servers/
│   ├── world_data_server.py
│   ├── weather_server.py
│   ├── finance_server.py
│   └── media_server.py
│
├── protocols/
│   └── message_models.py
│
├── ui/
│   └── app.py
│
├── shared/
│   └── config.py
│
├── .env.example
├── requirements.txt
└── README.md
```

---

# MCP Servers

The MCP servers expose contextual capabilities and tools over HTTP using FastAPI.

---

## 1. World Data MCP Server

### Purpose

Provides country and demographic information.

### Features

* Country lookup
* Population data
* Region information
* Capital city lookup

### Endpoint

```http
GET /country/{country}
```

### Example

```bash
http://localhost:8001/country/India
```

### Example Response

```json
{
  "name": "India",
  "capital": ["New Delhi"],
  "population": 1400000000,
  "region": "Asia"
}
```

---

## 2. Weather MCP Server

### Purpose

Provides live weather information using OpenWeatherMap API.

### Features

* Current temperature
* Humidity
* Wind speed
* Weather description

### Endpoint

```http
GET /weather/{city}
```

### Example

```bash
http://localhost:8002/weather/Bangalore
```

### Example Response

```json
{
  "city": "Bangalore",
  "temperature": 28.4,
  "humidity": 68,
  "weather": "scattered clouds",
  "wind_speed": 4.2
}
```

---

## 3. Finance MCP Server

### Purpose

Provides real-time finance and stock market information.

### Features

* Live stock prices
* High/low prices
* Open price
* Previous close
* Crypto endpoint placeholder

### Endpoint

```http
GET /stock/{symbol}
```

### Example

```bash
http://localhost:8003/stock/AAPL
```

### Example Response

```json
{
  "symbol": "AAPL",
  "current_price": 245.11,
  "high_price": 247.22,
  "low_price": 243.10,
  "open_price": 244.80,
  "previous_close": 242.90
}
```

---

## 4. Media MCP Server

### Purpose

Provides news and media aggregation.

### Features

* Topic-based news search
* Trending news
* Article metadata

### Endpoint

```http
GET /news/{topic}
```

### Example

```bash
http://localhost:8004/news/AI
```

### Example Response

```json
[
  {
    "title": "AI transforms enterprise workflows",
    "source": "TechCrunch"
  }
]
```

---

# Agents

The system contains multiple collaborating AI agents.

---

## 1. Contextualist Agent

### Responsibilities

* Fetch country information
* Fetch weather data
* Build contextual understanding

### MCP Calls

```python
requests.get("http://localhost:8001/country/India")
requests.get("http://localhost:8002/weather/Bangalore")
```

---

## 2. Scout Agent

### Responsibilities

* Fetch financial signals
* Fetch media/news signals
* Aggregate insights

### MCP Calls

```python
requests.get("http://localhost:8003/stock/AAPL")
requests.get("http://localhost:8004/news/AI")
```

---

## 3. Publisher Agent

### Responsibilities

* Combine all contextual data
* Generate AI article
* Produce final markdown output

### OpenAI Integration

Uses:

```python
client.chat.completions.create()
```

---

# Agent-to-Agent (A2A) Communication

Agents communicate using structured message payloads.

---

## Message Model

```python
class AgentMessage(BaseModel):
    sender: str
    receiver: str
    task: str
    payload: Dict[str, Any]
```

---

# Technology Stack

| Layer                 | Technology     |
| --------------------- | -------------- |
| Backend APIs          | FastAPI        |
| UI                    | Streamlit      |
| LLM                   | OpenAI         |
| MCP Communication     | HTTP REST APIs |
| Agent Framework       | Python         |
| Data Models           | Pydantic       |
| Environment Variables | python-dotenv  |

---

# Installation Guide

## Step 1: Download the Project

```bash
unzip multi_agent_mcp_system.zip
cd multi_agent_mcp_system
```

---

## Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Required Dependencies

```text
fastapi
uvicorn
streamlit
requests
python-dotenv
openai
pydantic
```

---

# API Keys Setup

## Create Environment File

Rename:

```bash
.env.example → .env
```

---

## Configure Keys

```env
OPENAI_API_KEY=your_openai_key
WEATHER_API_KEY=your_openweather_key
NEWS_API_KEY=your_newsapi_key
FINANCE_API_KEY=your_finnhub_key
```

---

# External APIs Used

| API            | Purpose             |
| -------------- | ------------------- |
| OpenAI         | Article generation  |
| OpenWeatherMap | Weather data        |
| NewsAPI        | News search         |
| Finnhub        | Finance data        |
| RestCountries  | Country information |

---

# Running the Project

The project requires multiple MCP servers running independently.

Open separate terminals.

---

# Run World Data MCP

```bash
uvicorn mcp_servers.world_data_server:app --reload --port 8001
```

---

# Run Weather MCP

```bash
uvicorn mcp_servers.weather_server:app --reload --port 8002
```

---

# Run Finance MCP

```bash
uvicorn mcp_servers.finance_server:app --reload --port 8003
```

---

# Run Media MCP

```bash
uvicorn mcp_servers.media_server:app --reload --port 8004
```

---

# Run Streamlit UI

```bash
streamlit run ui/app.py
```

---

# Application Workflow

## Step 1

User enters:

* Country
* City
* Topic
* Stock Symbol

---

## Step 2

Contextualist Agent gathers:

* Country context
* Weather context

---

## Step 3

Scout Agent gathers:

* News signals
* Finance signals

---

## Step 4

Publisher Agent:

* Combines context
* Uses OpenAI
* Generates article

---

## Step 5

Streamlit UI displays:

* Final article
* Context data
* Signals

---

# Example End-to-End Flow

```text
User Input
   ↓
Contextualist Agent
   ↓
Weather MCP + World MCP
   ↓
Scout Agent
   ↓
Finance MCP + Media MCP
   ↓
Publisher Agent
   ↓
OpenAI LLM
   ↓
Generated Article
```

---

# Example Usage

## Input

```text
Country: India
City: Bangalore
Topic: Artificial Intelligence
Stock: NVDA
```

---

## Output

```text
AI innovation in Bangalore continues to rise as NVIDIA stock gains momentum while technology investments increase globally...
```

---

# Why MCP Architecture?

MCP-style architecture provides:

* Modular tool design
* Independent scalability
* Easier maintenance
* Reusable services
* Distributed AI systems
* Agent interoperability

Each MCP server behaves as an independent contextual capability.

---

# Why Multi-Agent Systems?

Multi-agent systems allow:

* Specialized AI responsibilities
* Better reasoning decomposition
* Parallel task execution
* Scalable orchestration
* Autonomous workflows

---

# Advanced Improvements

## 1. Async FastAPI

Convert MCP endpoints to async.

---

## 2. Redis Pub/Sub

Add asynchronous messaging.

---

## 3. Kafka Event Streaming

Event-driven agent orchestration.

---

## 4. LangGraph Integration

Represent agents as graph nodes.

---

## 5. Vector Database Memory

Add:

* ChromaDB
* Pinecone
* Weaviate

---

## 6. Authentication

Add:

* JWT
* OAuth2
* API Gateway

---

## 7. Dockerization

Containerize each MCP server.

---

## 8. Kubernetes Deployment

Scale agents independently.

---

# Example Docker Commands

## Build

```bash
docker build -t multi-agent-system .
```

## Run

```bash
docker run -p 8501:8501 multi-agent-system
```

---

# Production Architecture Recommendation

```text
                ┌────────────────────┐
                │  API Gateway       │
                └─────────┬──────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
 ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
 │ Weather MCP │   │ Finance MCP │   │ Media MCP   │
 └─────────────┘   └─────────────┘   └─────────────┘

                          ▼
                ┌────────────────────┐
                │ Agent Orchestrator │
                └─────────┬──────────┘
                          │
            ┌─────────────┼─────────────┐
            │             │             │
            ▼             ▼             ▼
      Context Agent  Scout Agent  Publisher Agent
```

---

# Learning Outcomes

By completing this project, you will learn:

* FastAPI microservices
* MCP communication patterns
* Multi-agent architectures
* AI orchestration
* REST-based contextual tools
* Streamlit integration
* OpenAI API integration
* Real-time data aggregation
* Distributed AI systems

---

# Conclusion

This project provides a practical foundation for building:

* AI research assistants
* AI newsroom platforms
* Enterprise knowledge systems
* Autonomous AI ecosystems
* Financial intelligence systems
* Context-aware AI applications

The architecture is intentionally modular so additional MCP servers and AI agents can easily be added in the future.
