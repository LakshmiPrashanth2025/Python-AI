
from typing import Dict, Any


class SharedContext:
    def __init__(self, requirements: str):
        self.requirements = requirements

        # Architecture & Design
        self.architecture: Dict[str, Any] = {}
        self.api_contracts: Dict[str, Any] = {}
        self.database_schema: Dict[str, Any] = {}

        # Code Artifacts
        self.backend_code: Dict[str, Any] = {}
        self.service_code: Dict[str, Any] = {}
        self.frontend_code: Dict[str, Any] = {}

        # Quality
        self.validated_contracts: Dict[str, Any] = {}
        self.api_tests: Dict[str, Any] = {}
        self.security_policies: Dict[str, Any] = {}
        self.review_feedback: Dict[str, Any] = {}

        # DevOps
        self.dockerfiles: Dict[str, Any] = {}
        self.cicd_pipeline: Dict[str, Any] = {}
        self.terraform_code: Dict[str, Any] = {}

    def update(self, key: str, value: Any):
        setattr(self, key, value)

    def to_dict(self):
        return self.__dict__
