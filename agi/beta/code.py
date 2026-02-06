# agi

```json
{
    "files": [
        {
            "filename": "agent.py",
            "content": "# This is a basic example of an agent that interacts with the OpenAI API.\n\nimport openai\n\nclass Agent:\n    def __init__(self, api_key):\n        self.api_key = api_key\n        openai.api_key = self.api_key\n\n    def generate_response(self, prompt):\n        response = openai.Completion.create(\n            engine=\"text-davinci-003\",  # Replace with the desired engine\n            prompt=prompt,\n            max_tokens=150,\n            temperature=0.7\n        )\n        return response.choices[0].text\n\n# Example usage:\n# agent = Agent(\"your_api_key\")\n# response = agent.generate_response(\"What is the meaning of life?\")\n# print(response)"
        }
    ]
}
```
