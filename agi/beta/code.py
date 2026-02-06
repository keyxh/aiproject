# agi

```json
{
"files": [
{
"filename": "agent.py",
"content": "# agent.py\n\nimport openai\n\nclass Agent:\n    def __init__(self, api_key):\n        \"\"\"\n        Initializes the agent with an OpenAI API key.\n        \"\"\"\n        openai.api_key = api_key\n        self.memory = {}\n\n    def think(self, prompt):\n        \"\"\"\n        Processes a prompt, leveraging OpenAI's API for reasoning.\n\n        Args:\n            prompt: The input prompt for the agent.\n\n        Returns:\n            The agent's response.\n        \"\"\"\n        # Incorporate past interactions from memory\n        if self.memory:\n            prompt = f\"{self.memory.get('last_interaction', '')} You: {prompt}\"\n\n        response = openai.Completion.create(\n            engine=\"text-davinci-003\",  # Or a suitable OpenAI engine\n            prompt=prompt,\n            max_tokens=150,  # Adjust as needed\n            temperature=0.7  # Control creativity\n        )\n\n        response_text = response.choices[0].text.strip()\n\n        # Store interaction for context\n        self.memory['last_interaction'] = f\"Agent: {response_text}\"\n        return response_text\n\n# Example usage\n\nagent = Agent(\"YOUR_API_KEY\")\n\nwhile True:\n    user_input = input(\"You: \")\n    if user_input.lower() == \"exit\":\n        break\n    response = agent.think(user_input)\n    print(f\"Agent: {response}\")\n"
}
]
}
```
