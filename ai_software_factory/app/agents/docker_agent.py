
from app.core.base_agent import BaseAgent


class DockerAgent(BaseAgent):

    def run(self, context):

        prompt = f"""

Generate production Dockerfiles.

For:
- FastAPI backend
- React frontend

Include multi-stage builds.

"""

        result = self.llm.generate(prompt)


        context.update("dockerfiles", result)


        print("✔ DockerAgent completed")
        return context
