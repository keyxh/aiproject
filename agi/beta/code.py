# agi

```json
{
  "files": [
    {
      "filename": "agent.py",
      "content": "# This is a basic example of an agent that interacts with the OpenAI API.\n\nimport openai\n\nclass AGIAgent:\n    def __init__(self, api_key):\n        self.api_key = api_key\n        openai.api_key = self.api_key\n\n    def generate_response(self, prompt):\n        response = openai.Completion.create(\n            engine=\"text-davinci-003\",\n            prompt=prompt,\n            max_tokens=100,\n            n=1,\n            stop=None,\n            temperature=0.7\n        )\n        return response.choices[0].text\n\nif __name__ == '__main__':\n    agent = AGIAgent(\"YOUR_API_KEY\")\n    prompt = \"What is the meaning of life?\"\n    response = agent.generate_response(prompt)\n    print(response)"
    }
  ]
}
```
