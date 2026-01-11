# Multi-Agent AI System

This project implements a modular **multi-agent AI system** where specialized agents collaborate to solve a complex task under the control of a central orchestrator.  
The system demonstrates agentic architectures, shared state management, deterministic workflows, and observability through structured logging.

---

## 🧠 System Architecture Overview

The system consists of four main components:

### 1. Orchestrator
The **Orchestrator** is the central coordinator of the system. It:
- Accepts a single high-level user task
- Initializes shared state
- Executes agents in a deterministic sequence
- Maintains context across agents
- Determines when the task is complete
- Returns the final consolidated output

### 2. Researcher Agent
- Analyzes the user task
- Gathers key ideas and factual points
- Stores research notes in shared memory
- Does not generate final content

### 3. Writer Agent
- Uses research notes from shared state
- Produces a structured draft
- Focuses on clarity and coherence
- Does not critique or finalize

### 4. Critic Agent
- Reviews the draft content
- Improves clarity and completeness
- Produces the final polished output

---

## 🔄 Workflow Sequence

The workflow is deterministic and follows this order:

User Prompt
↓
Orchestrator
↓
Researcher Agent
↓
Writer Agent
↓
Critic Agent
↓
Final Output


Each agent reads from and writes to a **shared state object**, ensuring no loss of context.

---

## 🗂 Project Structure

multi-agent-ai-system/
│
├── agents/
│   ├── __init__.py
│   ├── base_agent.py
│   ├── researcher_agent.py
│   ├── writer_agent.py
│   └── critic_agent.py
│
├── orchestrator/
│   ├── __init__.py
│   └── orchestrator.py
│
├── memory/
│   ├── __init__.py
│   └── shared_state.py
│
├── logs/
│   └── system.log
│
├── example.py
├── requirements.txt
├── README.md
├── evaluation.md
└── architecture.png

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

git clone https://github.com/<your-username>/multi-agent-ai-system.git
cd multi-agent-ai-system

### 2. Create Virtual Environment

python -m venv venv

### 3. Activate Virtual Environment

Git Bash (Windows):

source venv/Scripts/activate

### 4. Install Dependencies

pip install -r requirements.txt

▶️ Running the System

Run the example script:

python example.py

### Example Task Executed

"Write a brief blog post about the benefits of multi-agent AI systems."

### Output

Final polished blog post printed to the terminal

Detailed execution logs saved in logs/system.log

🔍 Observability & Logging

The system implements structured logging to trace:

Agent execution order

Orchestrator decisions

Shared state transitions

Log format:

timestamp | agent_name | action_description

➕ Extensibility

New agents can be added by:

Extending BaseAgent

Implementing execute_task(shared_state)

Registering the agent in the orchestrator workflow

The modular design allows easy scalability.

✅ Key Features Demonstrated

Multi-agent collaboration

Deterministic orchestration

Shared memory management

Clear separation of concerns

Structured logging and observability

Modular and extensible architecture

