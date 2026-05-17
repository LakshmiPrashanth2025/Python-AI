
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class PublisherAgent:

    def generate_article(self, context, signals):

        prompt = f'''
        Create a professional article using:

        Context:
        {context}

        Signals:
        {signals}
        '''

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
