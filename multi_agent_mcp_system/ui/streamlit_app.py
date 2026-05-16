import streamlit as st
import requests

st.set_page_config(
    page_title="Multi-Agent MCP AI System",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# Helper Functions
# ---------------------------------------------------


def fetch_country_data(country):
    response = requests.get(
        f"http://localhost:8001/country/{country}"
    )
    return response.json()



def fetch_weather_data(city):
    response = requests.get(
        f"http://localhost:8002/weather/{city}"
    )
    return response.json()



def fetch_news(topic):
    response = requests.get(
        f"http://localhost:8004/news/{topic}"
    )
    return response.json()



def fetch_finance(stock_symbol):
    response = requests.get(
        f"http://localhost:8003/stock/{stock_symbol}"
    )
    return response.json()



def generate_article(context, signals):

    publisher_payload = {
        "context": context,
        "signals": signals
    }

    response = requests.post(
        "http://localhost:8010/generate-article",
        json=publisher_payload
    )

    return response.json().get("article", "No article generated")


# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("⚙️ MCP Agent Controls")

st.sidebar.markdown("""
### Active MCP Servers

| MCP Server | Port |
|---|---|
| World Data MCP | 8001 |
| Weather MCP | 8002 |
| Finance MCP | 8003 |
| Media MCP | 8004 |
""")

st.sidebar.markdown("---")

st.sidebar.info(
    "This Streamlit dashboard orchestrates multiple MCP servers and AI agents."
)

# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.title("🤖 Multi-Agent MCP AI System")

st.markdown(
    """
This application demonstrates:

- MCP-based contextual tools
- Agent-to-Agent orchestration
- FastAPI microservices
- Real-time data aggregation
- AI-generated articles
"""
)

# ---------------------------------------------------
# User Inputs
# ---------------------------------------------------

st.subheader("📥 User Inputs")

col1, col2 = st.columns(2)

with col1:
    country = st.text_input(
        "Country",
        placeholder="India"
    )

    topic = st.text_input(
        "Topic",
        placeholder="Artificial Intelligence"
    )

with col2:
    city = st.text_input(
        "City",
        placeholder="Bangalore"
    )

    stock_symbol = st.text_input(
        "Stock Symbol",
        value="NVDA"
    )

# ---------------------------------------------------
# Generate Workflow
# ---------------------------------------------------

if st.button("🚀 Generate AI Article", use_container_width=True):

    if not country or not city or not topic:
        st.error("Please fill all required inputs.")
        st.stop()

    try:

        with st.spinner("Contextualist Agent gathering context..."):

            country_data = fetch_country_data(country)
            weather_data = fetch_weather_data(city)

            context = {
                "country": country_data,
                "weather": weather_data
            }

        st.success("Contextualist Agent completed.")

        with st.spinner("Scout Agent aggregating signals..."):

            news_data = fetch_news(topic)
            finance_data = fetch_finance(stock_symbol)

            signals = {
                "news": news_data,
                "finance": finance_data
            }

        st.success("Scout Agent completed.")

        with st.spinner("Publisher Agent generating article..."):
            article = generate_article(
                context,
                signals
            )

        st.success("Publisher Agent completed.")

        # ---------------------------------------------------
        # Dashboard Metrics
        # ---------------------------------------------------

        st.subheader("📊 MCP Insights Dashboard")

        metric1, metric2, metric3, metric4 = st.columns(4)

        with metric1:
            st.metric(
                "Temperature",
                f"{weather_data.get('temperature', 'N/A')} °C"
            )

        with metric2:
            st.metric(
                "Humidity",
                f"{weather_data.get('humidity', 'N/A')} %"
            )

        with metric3:
            st.metric(
                "Stock Price",
                finance_data.get('current_price', 'N/A')
            )

        with metric4:
            st.metric(
                "News Articles",
                len(news_data)
            )

        # ---------------------------------------------------
        # Generated Article
        # ---------------------------------------------------

        st.subheader("📰 AI Generated Article")

        st.markdown(
            f"""
            <div style='padding:25px;border-radius:15px;background-color:#f8f9fa;'>
            {article}
            </div>
            """,
            unsafe_allow_html=True
        )

        # ---------------------------------------------------
        # Agent Outputs
        # ---------------------------------------------------

        col_a, col_b = st.columns(2)

        with col_a:
            with st.expander("🌍 Contextualist Agent Output"):
                st.json(context)

        with col_b:
            with st.expander("📡 Scout Agent Output"):
                st.json(signals)

        # ---------------------------------------------------
        # MCP Server Status
        # ---------------------------------------------------

        st.subheader("🧩 MCP Communication Flow")

        st.code(
            """
User Input
    ↓
Contextualist Agent
    ↓
World Data MCP (8001)
Weather MCP (8002)
    ↓
Scout Agent
    ↓
Finance MCP (8003)
Media MCP (8004)
    ↓
Publisher Agent
    ↓
AI Generated Article
            """
        )

    except Exception as e:
        st.error(f"System Error: {str(e)}")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.markdown("---")

st.caption(
    "Built using Streamlit, FastAPI, MCP Architecture, and Multi-Agent AI Orchestration"
)
