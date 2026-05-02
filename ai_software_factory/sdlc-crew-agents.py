from crewai import Agent, Crew, Task, Process
from crewai.tools import tool
import os
from dotenv import load_dotenv
from git import Repo

# ==============================
# ENV SETUP
# ==============================
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_ROUTER_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

# ==============================
# OUTPUT DIR
# ==============================
BASE_DIR = "generated_projects"
os.makedirs(BASE_DIR, exist_ok=True)

# ==============================
# TOOLS
# ==============================

@tool
def write_file(filepath: str, content: str) -> str:
    """Write content to a file"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Written: {filepath}"


@tool
def create_project_structure(project_name: str) -> str:
    """Create backend and frontend folders"""
    base_path = os.path.join(BASE_DIR, project_name)

    folders = [
        "backend/app",
        "frontend/src",
        "frontend/public"
    ]

    for f in folders:
        os.makedirs(os.path.join(base_path, f), exist_ok=True)

    return f"Created project structure at {base_path}"


@tool
def push_to_github(project_name: str) -> str:
    """Push project to GitHub"""
    local_path = os.path.join(BASE_DIR, project_name)

    repo = Repo.init(local_path)
    repo.git.add(all=True)
    repo.index.commit("Initial commit from AI Software Factory")

    remote_url = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{project_name}.git"

    try:
        origin = repo.create_remote("origin", remote_url)
    except:
        origin = repo.remote("origin")

    origin.push(refspec="master:master")

    return f"Pushed to GitHub: {project_name}"


# ==============================
# AGENTS
# ==============================

def create_agents():

    llm_model = "openrouter/openai/gpt-4o"

    return {
        "ba": Agent(
            role="Business Analyst",
            goal="Analyze requirements",
            backstory="Expert in business requirements",
            verbose=True,
            llm=llm_model
        ),

        "pm": Agent(
            role="Product Manager",
            goal="Create product roadmap and PRD",
            backstory="Product expert",
            verbose=True,
            llm=llm_model
        ),

        "architect": Agent(
            role="Software Architect",
            goal="Design scalable architecture",
            backstory="System design expert",
            verbose=True,
            llm=llm_model
        ),

        "developer": Agent(
            role="Full Stack Developer",
            goal="Generate backend and frontend code",
            backstory="Expert in FastAPI and React",
            tools=[write_file, create_project_structure],
            verbose=True,
            llm=llm_model
        ),

        "devops": Agent(
            role="DevOps Engineer",
            goal="Push code to GitHub",
            backstory="CI/CD expert",
            tools=[push_to_github],
            verbose=True,
            llm=llm_model
        )
    }


# ==============================
# TASKS
# ==============================

def create_tasks(agents, project_name, app_idea):

    base_path = f"{BASE_DIR}/{project_name}"

    t1 = Task(
        description=f"Analyze requirements for: {app_idea}",
        expected_output="Business requirements document",
        output_file=f"{base_path}/business_requirements.md",
        agent=agents["ba"]
    )

    t2 = Task(
        description="Create product requirements document",
        expected_output="PRD",
        output_file=f"{base_path}/product_requirements.md",
        agent=agents["pm"],
        context=[t1]
    )

    t3 = Task(
        description="Design system architecture",
        expected_output="Architecture document",
        output_file=f"{base_path}/architecture.md",
        agent=agents["architect"],
        context=[t2]
    )

    #  Create project structure
    t4 = Task(
        description=f"""
        Create project structure for {project_name}
        Use create_project_structure tool
        """,
        expected_output="Folders created",
        agent=agents["developer"]
    )

    #  Backend
    t5 = Task(
        description=f"""
        Create FastAPI backend for {project_name}

        MUST:
        - Use write_file tool
        - Create:
          {base_path}/backend/app/main.py
          {base_path}/backend/app/routes.py
          {base_path}/backend/app/models.py
        """,
        expected_output="Backend code created",
        agent=agents["developer"],
        context=[t3]
    )

    # Frontend
    t6 = Task(
        description=f"""
        Create React frontend

        MUST:
        - Use write_file tool
        - Create:
          {base_path}/frontend/src/App.jsx
        """,
        expected_output="Frontend created",
        agent=agents["developer"],
        context=[t5]
    )

    # 🔥 GitHub push
    t7 = Task(
        description=f"""
        Push project to GitHub

        repo name: {project_name}
        """,
        expected_output="Repo pushed",
        agent=agents["devops"],
        context=[t6]
    )

    return [t1, t2, t3, t4, t5, t6, t7]


# ==============================
# RUNNER
# ==============================

def run_sdlc_crew(app_idea: str, project_name: str):

    agents = create_agents()
    tasks = create_tasks(agents, project_name, app_idea)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n✅ DONE!")
    print(f"📁 Project: {BASE_DIR}/{project_name}")

    return result


# ==============================
# MAIN
# ==============================

if __name__ == "__main__":

    app_idea = """
    Build a task management app with:
    - login
    - task tracking
    - dashboard
    """

    project_name = "ai_task_manager"

    run_sdlc_crew(app_idea, project_name)
