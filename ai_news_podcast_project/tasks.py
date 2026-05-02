from crewai import Task
from agents import research_agent, script_agent, podcast_agent, linkedin_agent

research_task = Task(
    description="Search for breaking AI news from the past 24 hours and summarize key updates.",
    agent=research_agent
)

script_task = Task(
    description="Create an engaging 5-minute AI news podcast script with intro, insights, and outro.",
    agent=script_agent
)

podcast_task = Task(
    description="Convert the script into natural spoken format ready for narration.",
    agent=podcast_agent
)

linkedin_task = Task(
    description="Write a compelling LinkedIn post promoting today's AI podcast. Add hook and CTA.",
    agent=linkedin_agent
)
