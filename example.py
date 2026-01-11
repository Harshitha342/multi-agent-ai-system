from orchestrator.orchestrator import Orchestrator


def main():
    # High-level user prompt (single entry point)
    user_task = (
        "Write a brief blog post about the benefits of multi-agent AI systems."
    )

    # Initialize orchestrator
    orchestrator = Orchestrator(user_task)

    # Run the workflow
    final_output = orchestrator.run()

    # Display final result
    print("\n" + "=" * 50)
    print("FINAL OUTPUT")
    print("=" * 50 + "\n")
    print(final_output)


if __name__ == "__main__":
    main()
