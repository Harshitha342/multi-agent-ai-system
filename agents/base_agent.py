from abc import ABC, abstractmethod
import logging


class BaseAgent(ABC):
    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        self.logger = logging.getLogger(self.name)

    @abstractmethod
    def execute_task(self, shared_state):
        pass
