
from app.core.base_agent import BaseAgent


class FrontendAgent(BaseAgent):

    def run(self, context):

        prompt = f"""

Generate a production-ready ReactJS frontend.

Use:
API Contracts:
{context.validated_contracts}

Requirements:
{context.requirements}

Include:
- Axios service layer
- Routing
- Forms
- Validation
- Error handling
- Clean folder structure

"""

        result = self.llm.generate(prompt)


        context.update("frontend_code", result)


        print("✔ FrontendAgent completed")
        return context
