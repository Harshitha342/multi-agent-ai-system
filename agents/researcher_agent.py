from agents.base_agent import BaseAgent


class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ResearcherAgent",
            system_prompt="You research and collect key points."
        )

    def execute_task(self, shared_state):
        self.logger.info("Starting research")

        task = shared_state.get("user_task")

        research_notes = (
            f"Key points about the task '{task}':\n"
            "- Multi-agent systems divide complex tasks\n"
            "- Specialized agents improve quality\n"
            "- Orchestration ensures coordination\n"
            "- Shared memory prevents context loss\n"
        )

        shared_state.update("research_notes", research_notes)

        self.logger.info("Research completed")
        return shared_state
