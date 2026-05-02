
from app.core.base_agent import BaseAgent


class ApiTestAgent(BaseAgent):

    def run(self, context):

        prompt = f"""

Generate pytest test suite.

Use:
OpenAPI Spec:
{context.validated_contracts}

Include:
- Unit tests
- Integration tests
- Auth tests
- Edge cases

"""

        result = self.llm.generate(prompt)


        context.update("api_tests", result)


        print("✔ ApiTestAgent completed")
        return context
