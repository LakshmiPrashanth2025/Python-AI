
from app.core.orchestrator import Orchestrator

if __name__ == "__main__":
    requirements = """
Build a task management system:
- User authentication
- CRUD tasks
- Due dates
- Mark complete
"""

    orchestrator = Orchestrator()
    orchestrator.run(requirements)

    print("AI Software Factory execution complete.")
