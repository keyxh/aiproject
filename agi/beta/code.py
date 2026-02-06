# agi

{
    "files": [
        {
            "filename": "requirements.txt",
            "content": "openai>=1.0.0\npython-dotenv"
        },
        {
            "filename": ".env.example",
            "content": "OPENAI_API_KEY=your_api_key_here"
        },
        {
            "filename": "config.py",
            "content": "import os\nfrom dotenv import load_dotenv\n\n# Load environment variables from .env file\nload_dotenv()\n\n# Fetch OpenAI API key from environment variables\nOPENAI_API_KEY = os.getenv(\"OPENAI_API_KEY\")\nif not OPENAI_API_KEY:\n    raise ValueError(\"Please set OPENAI_API_KEY in .env file\")\n"
        },
        {
            "filename": "memory.py",
            "content": "class Memory:\n    \"\"\"\n    A simple memory class to store conversation history.\n    \"\"\"\n    def __init__(self):\n        self.memories = []\n    \n    def add(self, user_input: str, agent_response: str):\n        \"\"\"Add a new conversation entry to memory.\"\"\"\n        self.memories.append({\"user\": user_input, \"agent\": agent_response})\n    \n    def get_recent(self, n: int = 5):\n        \"\"\"Retrieve the most recent n conversation entries.\"\"\"\n        return self.memories[-n:] if len(self.memories) >= n else self.memories\n"
        },
        {
            "filename": "tools.py",
            "content": "def search_web(query: str) -> str:\n    \"\"\"\n    Simulate a web search tool.\n    In a real implementation, integrate with an actual search API.\n    \"\"\"\n    return f\"Search results for '{query}': Simulated data.\"\n\n\ndef calculate(expression: str) -> str:\n    \"\"\"\n    A simple calculator tool.\n    Warning: eval() is used for demonstration; avoid in production for security.\n    \"\"\"\n    try:\n        result = eval(expression)  # For demo only; use safer alternatives in production\n        return f\"Result: {result}\"\n    except Exception as e:\n        return f\"Error: {e}\"\n"
        },
        {
            "filename": "agent.py",
            "content": "import openai\nfrom memory import Memory\nfrom typing import List, Callable\n\nclass AGIAgent:\n    \"\"\"\n    AGI Agent class that uses OpenAI API for core intelligence,\n    with memory and tool integration.\n    \"\"\"\n    def __init__(self, api_key: str):\n        # Initialize OpenAI client\n        self.client = openai.OpenAI(api_key=api_key)\n        self.memory = Memory()  # Memory instance for conversation history\n        self.tools: List[Callable] = []  # List of available tools\n    \n    def add_tool(self, tool: Callable):\n        \"\"\"Add a tool function to the agent's toolkit.\"\"\"\n        self.tools.append(tool)\n    \n    def process_input(self, user_input: str) -> str:\n        \"\"\"\n        Process user input: build context, call OpenAI model, and update memory.\n        Returns the agent's response.\n        \"\"\"\n        # Build context from recent memory\n        context = self._build_context()\n        prompt = f\"{context}\\nUser: {user_input}\\nAgent:\"\n        \n        # Call OpenAI API (using GPT-4 as an example)\n        try:\n            response = self.client.chat.completions.create(\n                model=\"gpt-4\",  # Can be changed to other models like gpt-3.5-turbo\n                messages=[\n                    {\"role\": \"system\", \"content\": \"You are a helpful AGI agent capable of using tools and remembering conversations.\"},\n                    {\"role\": \"user\", \"content\": prompt}\n                ],\n                max_tokens=500  # Adjust as needed\n            )\n            output = response.choices[0].message.content\n        except Exception as e:\n            output = f\"Error calling OpenAI API: {e}\"\n        \n        # Update memory with the new interaction\n        self.memory.add(user_input, output)\n        \n        return output\n    \n    def _build_context(self) -> str:\n        \"\"\"Build a context string from recent memory entries.\"\"\"\n        recent = self.memory.get_recent(5)  # Get last 5 entries\n        if not recent:\n            return \"No previous conversation.\"\n        context = \"Previous conversation:\\n\"\n        for entry in recent:\n            context += f\"User: {entry['user']}\\nAgent: {entry['agent']}\\n\"\n        return context\n"
        },
        {
            "filename": "main.py",
            "content": "from config import OPENAI_API_KEY\nfrom agent import AGIAgent\nfrom tools import search_web, calculate\n\ndef main():\n    \"\"\"Main function to run the AGI agent in a loop.\"\"\"\n    # Initialize AGI agent with API key\n    agent = AGIAgent(api_key=OPENAI_API_KEY)\n    \n    # Add example tools to the agent\n    agent.add_tool(search_web)\n    agent.add_tool(calculate)\n    \n    print(\"AGI Agent started. Type 'exit' to quit.\")\n    while True:\n        user_input = input(\"You: \")\n        if user_input.lower() == 'exit':\n            print(\"Goodbye!\")\n            break\n        response = agent.process_input(user_input)\n        print(f\"Agent: {response}\")\n\nif __name__ == \"__main__\":\n    main()\n"
        },
        {
            "filename": "README.md",
            "content": "# AGI Project\n\nThis project implements a basic Artificial General Intelligence (AGI) agent using OpenAI API. It includes memory management, tool integration, and interactive conversation capabilities.\n\n## Features\n- Uses OpenAI's GPT-4 model for core intelligence.\n- Maintains conversation memory for context.\n- Supports extensible tools (e.g., web search simulation, calculator).\n- Interactive command-line interface.\n\n## Setup\n1. **Install dependencies:**\n   ```bash\n   pip install -r requirements.txt\n   ```\n2. **Set up environment variables:**\n   - Create a `.env` file in the project root.\n   - Add your OpenAI API key: `OPENAI_API_KEY=your_key_here`.\n   - Refer to `.env.example` for guidance.\n3. **Run the agent:**\n   ```bash\n   python main.py\n   ```\n\n## Usage\n- Start the agent, and interact via the terminal.\n- Type `exit` to quit the session.\n- The agent uses recent conversation history to provide context-aware responses.\n\n## Project Structure\n- `main.py`: Entry point for the agent.\n- `agent.py`: Defines the AGIAgent class with core logic.\n- `memory.py`: Manages conversation memory.\n- `tools.py`: Contains example tools for the agent.\n- `config.py`: Handles configuration