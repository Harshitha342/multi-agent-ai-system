import logging

from agents.researcher_agent import ResearcherAgent
from agents.writer_agent import WriterAgent
from agents.critic_agent import CriticAgent
from memory.shared_state import SharedState


# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/system.log"),
        logging.StreamHandler()
    ]
)


class Orchestrator:
    """
    Central coordinator responsible for managing agent workflow
    and shared state.
    """

    def __init__(self, user_task: str):
        self.logger = logging.getLogger("Orchestrator")
        self.shared_state = SharedState(user_task)

        # Initialize agents
        self.researcher = ResearcherAgent()
        self.writer = WriterAgent()
        self.critic = CriticAgent()

    def run(self):
        """
        Runs the deterministic agent workflow:
        Researcher -> Writer -> Critic
        """
        self.logger.info("Workflow started")
        self.logger.info(f"User task: {self.shared_state.get('user_task')}")

        # Step 1: Research
        self.logger.info("Sending task to ResearcherAgent")
        self.researcher.execute_task(self.shared_state)

        # Step 2: Writing
        self.logger.info("Sending task to WriterAgent")
        self.writer.execute_task(self.shared_state)

        # Step 3: Critique & Finalization
        self.logger.info("Sending task to CriticAgent")
        self.critic.execute_task(self.shared_state)

        self.logger.info("Workflow completed")

        return self.shared_state.get("final_output")
