
from app.core.base_agent import BaseAgent


class CicdAgent(BaseAgent):

    def run(self, context):

        prompt = f"""

Generate GitHub Actions CI/CD pipeline.

Include:
- Lint
- Tests
- Docker build
- Deploy

"""

        result = self.llm.generate(prompt)


        context.update("cicd_pipeline", result)


        print("✔ CicdAgent completed")
        return context
