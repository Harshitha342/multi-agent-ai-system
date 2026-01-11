class SharedState:
    def __init__(self, user_task: str):
        self.state = {
            "user_task": user_task,
            "research_notes": "",
            "draft_content": "",
            "critic_feedback": "",
            "final_output": ""
        }

    def update(self, key, value):
        self.state[key] = value

    def get(self, key):
        return self.state.get(key)

    def get_all(self):
        return self.state
