
class BaseAgent:
    def __init__(self, name: str, llm):
        self.name = name
        self.llm = llm

    def run(self, context):
        raise NotImplementedError
