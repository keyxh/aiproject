# agi

```json
{
  "files": [
    {
      "filename": "agent.py",
      "content": "# agent.py\n\nimport openai\n\nclass AGIAgent:\n    def __init__(self, api_key):\n        openai.api_key = api_key\n        self.memory = ''\n\n    def process_input(self, user_input):\n        \"\"\"Processes user input and generates a response.\"\"\"\n        prompt = f\"{self.memory}User: {user_input}\\nAssistant:\"\n        response = openai.Completion.create(\n            engine=\"text-davinci-003\",\n            prompt=prompt,\n            max_tokens=150,\n            temperature=0.7\n        )\n        self.memory += f\"User: {user_input}\\nAssistant: {response.choices[0].text}\\n\"\n        return response.choices[0].text\n\n# Example usage\nagent = AGIAgent(\"YOUR_API_KEY\")\nwhile True:\n    user_input = input(\"You: \")\n    if user_input.lower() == 'quit':\n        break\n    response = agent.process_input(user_input)\n    print(\"Assistant: \", response)"
    }
  ]
}
```
