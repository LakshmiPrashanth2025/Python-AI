from crewai import Crew
from tasks import research_task, script_task, podcast_task, linkedin_task
from tts import create_podcast_audio
from linkedin import post_to_linkedin

crew = Crew(
    agents=[
        research_task.agent,
        script_task.agent,
        podcast_task.agent
        # ,
        # linkedin_task.agent
    ],
    tasks=[research_task, script_task, podcast_task, linkedin_task],
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff()

    print("\nPodcast Script:\n")
    print(result)

    create_podcast_audio(result)
    print("Podcast saved as podcast.mp3")

    # Generate LinkedIn caption
    linkedin_caption = linkedin_task.execute()
    post_to_linkedin(linkedin_caption)
