
from app.core.base_agent import BaseAgent


class ContractValidationAgent(BaseAgent):

    def run(self, context):

        prompt = f"""

Validate API contracts.

Requirements:
{context.requirements}

OpenAPI Spec:
{context.architecture}

Ensure:
- Endpoints match requirements
- DB schema consistency
- Proper HTTP verbs
- Correct request/response models

Return corrected OpenAPI spec.

"""

        result = self.llm.generate(prompt)


        context.update("validated_contracts", result)


        print("✔ ContractValidationAgent completed")
        return context
