
from app.core.base_agent import BaseAgent


class SecurityAgent(BaseAgent):

    def run(self, context):

        prompt = f"""

Enhance backend security.

Backend Code:
{context.backend_code}

Add:
- JWT authentication
- RBAC
- Input validation
- CORS config
- Rate limiting
- Secure headers

"""

        result = self.llm.generate(prompt)


        context.update("backend_code", result)
        context.update("security_policies", "JWT + RBAC + Rate limiting")


        print("✔ SecurityAgent completed")
        return context
