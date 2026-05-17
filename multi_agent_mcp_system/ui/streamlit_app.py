
import streamlit as st

from agents.contextualist_agent import ContextualistAgent
from agents.scout_agent import ScoutAgent
from agents.publisher_agent import PublisherAgent

st.title("Multi-Agent MCP AI System")

country = st.text_input("Country")
city = st.text_input("City")
topic = st.text_input("Topic")
stock = st.text_input("Stock Symbol", "AAPL")

if st.button("Generate Article"):

    contextualist = ContextualistAgent()
    scout = ScoutAgent()
    publisher = PublisherAgent()

    with st.spinner("Agents collaborating..."):

        context = contextualist.fetch_context(country, city)

        signals = scout.aggregate_signals(
            topic,
            stock
        )

        article = publisher.generate_article(
            context,
            signals
        )

    st.subheader("Generated Article")
    st.markdown(article)

    with st.expander("Context Data"):
        st.json(context)

    with st.expander("Signals"):
        st.json(signals)
