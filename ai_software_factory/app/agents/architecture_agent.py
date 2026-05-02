
from app.core.base_agent import BaseAgent


class ArchitectureAgent(BaseAgent):

    def run(self, context):

        prompt = f"""

You are a Senior Software Architect.

Requirements:
{context.requirements}

Design:
1. System architecture (monolith or microservices)
2. Database schema (Postgres)
3. OpenAPI 3.0 specification
4. Service boundaries

Output:
- JSON structure with keys:
  architecture
  database_schema
  openapi_spec

"""

        result = self.llm.generate(prompt)


        context.update("architecture", result)


        print("✔ ArchitectureAgent completed")
        return context
