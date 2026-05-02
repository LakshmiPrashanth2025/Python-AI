from crewai import Agent
from tools import SerperAINewsTool

news_tool = SerperAINewsTool()

research_agent = Agent(
    role="AI News Researcher",
    goal="Find and summarize latest AI news",
    backstory="Tech journalist specializing in AI trends",
    tools=[news_tool],
    verbose=True
)

script_agent = Agent(
    role="Podcast Script Writer",
    goal="Write an engaging 5-minute AI news podcast script",
    backstory="Professional tech podcast writer",
    verbose=True
)

podcast_agent = Agent(
    role="Podcast Host",
    goal="Convert script into natural spoken-word format",
    backstory="Charismatic AI podcast host",
    verbose=True
)

linkedin_agent = Agent(
    role="LinkedIn Content Strategist",
    goal="Write a high-engagement LinkedIn post promoting the podcast",
    backstory="Expert in AI personal branding",
    verbose=True
)
