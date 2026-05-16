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
│   ├── app.py
│   └── streamlit_app.py
│
├── shared/
│   └── config.py
│
├── .env.example
├── requirements.txt
└── README.md
```

---

# Streamlit User Interface

The project includes an enhanced Streamlit dashboard located at:

```text
ui/streamlit_app.py
```

The Streamlit dashboard acts as the frontend orchestration layer for the Multi-Agent MCP system.

It communicates with:

* World Data MCP
* Weather MCP
* Finance MCP
* Media MCP
* Publisher Agent API

---

# Streamlit UI Features

| Feature | Description |
|---|---|
| MCP Dashboard | Displays orchestration flow |
| Country Input | Contextual country information |
| City Input | Weather lookup |
| Topic Input | News/media search |
| Stock Symbol Input | Finance lookup |
| Real-Time Agent Status | Displays workflow progress |
| Metrics Dashboard | Weather + finance insights |
| Context Viewer | Displays contextual agent data |
| Signal Viewer | Displays Scout Agent outputs |
| AI Article Rendering | Displays generated article |
| MCP Communication Flow | Visualizes orchestration |

---

# Streamlit UI Workflow

```text
User Inputs
    ↓
Streamlit UI
    ↓
Contextualist Agent
    ↓
World MCP + Weather MCP
    ↓
Scout Agent
    ↓
Finance MCP + Media MCP
    ↓
Publisher Agent
    ↓
Generated AI Article
```

---

# Streamlit UI MCP Communication

The Streamlit UI communicates directly with FastAPI MCP servers using REST APIs.

### Example MCP Calls

```python
requests.get("http://localhost:8001/country/India")
requests.get("http://localhost:8002/weather/Bangalore")
requests.get("http://localhost:8003/stock/NVDA")
requests.get("http://localhost:8004/news/AI")
```

---

# Streamlit Dashboard Code

File:

```text
ui/streamlit_app.py
```

### Main Responsibilities

* Gather user inputs
* Trigger MCP workflows
* Display contextual insights
* Render AI-generated article
* Visualize orchestration flow

---

# Running the Streamlit UI

## Command

```bash
streamlit run ui/streamlit_app.py
```

---

# Streamlit Default URL

```text
http://localhost:8501
```

---

# Example Streamlit Inputs

| Field | Example |
|---|---|
| Country | India |
| City | Bangalore |
| Topic | Artificial Intelligence |
| Stock Symbol | NVDA |

---

# Example Streamlit Output

```text
AI innovation in Bangalore continues to rise as NVIDIA stock gains momentum while technology investments increase globally...
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
