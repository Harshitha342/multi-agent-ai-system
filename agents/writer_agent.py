from agents.base_agent import BaseAgent


class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="WriterAgent",
            system_prompt="You write clear and engaging content."
        )

    def execute_task(self, shared_state):
        self.logger.info("Starting writing")

        research = shared_state.get("research_notes")

        draft = (
            "Multi-agent AI systems are powerful because they break down "
            "complex problems into smaller tasks handled by specialized agents. "
            "Each agent focuses on a specific responsibility, such as research "
            "or content creation, resulting in higher-quality outputs. "
            "An orchestrator coordinates these agents, while shared memory "
            "ensures consistency across the workflow."
        )

        shared_state.update("draft_content", draft)

        self.logger.info("Draft created")
        return shared_state
