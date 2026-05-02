
from app.core.base_agent import BaseAgent


class BackendAgent(BaseAgent):

    def run(self, context):

        prompt = f"""

Generate a complete FastAPI backend.

Use:
OpenAPI Spec:
{context.validated_contracts}

Database Schema:
{context.database_schema}

Requirements:
{context.requirements}

Generate:
- main.py
- routers
- models
- Pydantic schemas
- database connection
- CRUD operations

Production ready.

"""

        result = self.llm.generate(prompt)


        context.update("backend_code", result)


        print("✔ BackendAgent completed")
        return context
