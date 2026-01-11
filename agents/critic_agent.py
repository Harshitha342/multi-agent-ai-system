from agents.base_agent import BaseAgent


class CriticAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="CriticAgent",
            system_prompt="You critique and improve content."
        )

    def execute_task(self, shared_state):
        self.logger.info("Starting critique")

        draft = shared_state.get("draft_content")

        improved = (
            draft +
            "\n\nOverall, multi-agent systems demonstrate how collaboration "
            "between AI components leads to more reliable and scalable solutions."
        )

        shared_state.update("final_output", improved)

        self.logger.info("Critique completed")
        return shared_state
