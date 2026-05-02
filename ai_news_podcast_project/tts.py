import edge_tts
import asyncio

async def generate_audio(text, filename="podcast.mp3"):
    communicate = edge_tts.Communicate(text, voice="en-US-AriaNeural")
    await communicate.save(filename)

def create_podcast_audio(text):
    asyncio.run(generate_audio(text))
