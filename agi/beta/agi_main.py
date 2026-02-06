import os
from core.agi_system import AGISystem
from core.config import Config

def main():
    # Load configuration
    config = Config()
    
    # Initialize AGI system
    agi = AGISystem(config)
    
    # Start the main loop
    agi.start()

if __name__ == "__main__":
    main()