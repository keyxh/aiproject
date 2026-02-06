from agent import AIAgent

def main():
    """
    Main function to run the AGI system.
    Initializes the AI agent and starts an interactive chat loop.
    """
    agent = AIAgent()
    
    print("AGI System Initialized. Type 'exit' to quit.")
    
    while True:
        try:
            user_input = input("You: ")
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting.")
            break
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = agent.chat(user_input)
        print(f"AGI: {response}")

if __name__ == "__main__":
    main()
