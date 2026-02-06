# agi

```json
{
    "files": [
        {
            "filename": "agent.py",
            "content": "from openai import OpenAI\n\nclass AGIAgent:\n    def __init__(self, api_key):\n        self.client = OpenAI(api_key=api_key)\n\n    def process_input(self, user_input):\n        \"\"\"\n        Processes user input and generates a response using the OpenAI API.\n\n        Args:\n            user_input: The user's input text.\n\n        Returns:\n            The agent's response text.\n        \"\"\"\n        response = self.client.chat.completions.create(\n            model=\"gpt-3.5-turbo\",\n            messages=[{\"role\": \"user\", \"content\": user_input}],\n            temperature=0.7\n        )\n        return response.choices[0].message.content\n\nif __name__ == \"__main__\":\n    api_key = \"YOUR_API_KEY\"\n    agent = AGIAgent(api_key)\n    while True:\n        user_input = input(\"You: \")\n        if user_input.lower() == \"exit\":\n            break\n        response = agent.process_input(user_input)\n        print(\"Agent: \" + response)"
        }
    ]
}
```
