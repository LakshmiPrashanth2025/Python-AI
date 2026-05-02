
from app.core.context import SharedContext
from app.llm.llm_provider import LLMProvider

from app.agents.architecture_agent import ArchitectureAgent
from app.agents.contract_validation_agent import ContractValidationAgent
from app.agents.backend_agent import BackendAgent
from app.agents.security_agent import SecurityAgent
from app.agents.api_test_agent import ApiTestAgent
from app.agents.frontend_agent import FrontendAgent
from app.agents.docker_agent import DockerAgent
from app.agents.cicd_agent import CicdAgent
from app.agents.terraform_agent import TerraformAgent


class Orchestrator:

    def __init__(self):
        llm = LLMProvider()
        self.agents = [
            ArchitectureAgent("Architecture", llm),
            ContractValidationAgent("ContractValidation", llm),
            BackendAgent("Backend", llm),
            SecurityAgent("Security", llm),
            ApiTestAgent("Tests", llm),
            FrontendAgent("Frontend", llm),
            DockerAgent("Docker", llm),
            CicdAgent("CICD", llm),
            TerraformAgent("Terraform", llm),
        ]

    def run(self, requirements: str):
        context = SharedContext(requirements)

        for agent in self.agents:
            context = agent.run(context)

        return context
