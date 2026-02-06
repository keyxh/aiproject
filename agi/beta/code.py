# agi

```json
{
  "files": [
    {
      "filename": "agent.py",
      "content": "# This is a basic example of an agent that uses the OpenAI API.\n\nimport openai\n\n# Set your OpenAI API key\nopenai.api_key = \"YOUR_API_KEY\"\n\nclass Agent:\n    def __init__(self):\n        pass\n\n    def act(self, observation):\n        \"\"\"\n        Takes an observation as input and returns an action.\n\n        Args:\n            observation: A string representing the current observation.\n\n        Returns:\n            A string representing the action to take.\n        \"\"\"\n        # This is a very simple agent that just echoes the observation\n        # as the action.\n        return observation\n\n# Example usage\nagent = Agent()\nobservation = \"Hello, world!\"\naction = agent.act(observation)\nprint(f\"Observation: {observation}\")\nprint(f\"Action: {action}\")\n"
    }
  ]
}
```
