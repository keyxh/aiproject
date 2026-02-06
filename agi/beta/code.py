# agi

```json
{
  "files": [
    {
      "filename": "agent.py",
      "content": "# agent.py\n\nimport openai\n\nclass AGIAgent:\n    def __init__(self, api_key):\n        \"\"\"\n        Initializes the AGI agent with an OpenAI API key.\n\n        Args:\n            api_key: The OpenAI API key.\n        \"\"\"\n        openai.api_key = api_key\n        self.memory = []  # Initialize memory to store context\n\n    def process_input(self, user_input):\n        \"\"\"\n        Processes user input, interacts with the OpenAI API, and generates a response.\n\n        Args:\n            user_input: The user's input string.\n\n        Returns:\n            The agent's response string.\n        \"\"\"\n        context = \"\\n\".join(self.memory) + \"\\nUser: \" + user_input\n        response = openai.Completion.create(\n          engine=\"text-davinci-003\",  # Or another suitable engine\n          prompt=context,\n          max_tokens=150  # Adjust as needed\n        )\n        agent_response = response.choices[0].text.strip()\n        self.memory.append(f\"Agent: {agent_response}\")\n        return agent_response\n\n# Example usage:\n# agent = AGIAgent(\"YOUR_API_KEY\")\n# while True:\n#     user_input = input(\"You: \")\n#     response = agent.process_input(user_input)\n#     print(\"Agent: \", response)"
    }
  ]
}

```
