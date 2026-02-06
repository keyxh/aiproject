# agi

```json
{
  "files": [
    {
      "filename": "agent.py",
      "content": "# agent.py\n\nimport openai\n\nclass AGIAgent:\n    def __init__(self, api_key):\n        openai.api_key = api_key\n        self.memory = []\n\n    def process_input(self, user_input):\n        self.memory.append(user_input)\n        context = '\\n'.join(self.memory[-10:])  # Use last 10 interactions\n        \n        response = openai.Completion.create(\n            engine=\"text-davinci-003\",  # Choose a suitable OpenAI model\n            prompt=f\"Context: {context}\\nUser: {user_input}\\nAI:\",\n            max_tokens=150,\n            temperature=0.7\n        )\n\n        return response.choices[0].text\n\n# Example usage\nag = AGIAgent(\"your_openai_api_key\")\n\nwhile True:\n    user_input = input(\"You: \")\n    if user_input.lower() == \"exit\":\n        break\n    response = ag.process_input(user_input)\n    print(\"AGI:\", response)"
    }
  ]
}
```
