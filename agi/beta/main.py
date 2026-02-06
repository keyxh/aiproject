"""
Main entry point for the AGI system

This script demonstrates how to use the AGI core module to perform various tasks.
"""

import asyncio
import sys
from agi_core import AGI

async def main():
    print("Initializing AGI System...")
    
    # Create AGI instance
    agi = AGI(model_name="gpt-4", max_retries=3)
    
    # Load previous state if available
    try:
        agi.load_state("agi_state.json")
        print("Loaded previous AGI state")
    except Exception as e:
        print(f"Could not load state: {e}")
    
    # Example tasks
    tasks = [
        "Explain the concept of artificial general intelligence in simple terms",
        "Write a short story about an AI that learns to feel emotions",
        "Analyze the potential risks and benefits of developing a true AGI",
        "Plan a week-long trip to Japan including budget estimates and cultural tips"
    ]
    
    print("Starting task execution...")
    results = await agi.run(tasks)
    
    # Display results
    print("\n=== TASK RESULTS ===")
    for task in results:
        print(f"Task ID: {task.id}")
        print(f"Description: {task.description}")
        print(f"Status: {task.status.value}")
        if task.result:
            print(f"Result: {task.result[:200]}...")
        print("---")
    
    # Perform self-reflection
    print("\nPerforming self-reflection...")
    reflection = await agi.self_reflection()
    print(f"Self-reflection:\n{reflection}")
    
    # Show task summary
    summary = agi.get_task_summary()
    print(f"\n=== TASK SUMMARY ===\n{summary}")
    
    # Save current state
    agi.save_state("agi_state.json")
    print("\nAGI state saved.")
    
    # Wait a moment before exiting
    await asyncio.sleep(2)
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nAGI system interrupted by user.")
    except Exception as e:
        print(f"Error running AGI system: {e}", file=sys.stderr)
        sys.exit(1)