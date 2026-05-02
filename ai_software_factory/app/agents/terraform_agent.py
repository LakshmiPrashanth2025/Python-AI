
from app.core.base_agent import BaseAgent


class TerraformAgent(BaseAgent):

    def run(self, context):

        prompt = f"""

Generate Terraform AWS infrastructure.

Include:
- ECS
- RDS
- VPC
- ALB
- Auto scaling

"""

        result = self.llm.generate(prompt)


        context.update("terraform_code", result)


        print("✔ TerraformAgent completed")
        return context
