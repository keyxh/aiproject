# agi

```json
{
  "files": [
    {
      "filename": "agent.py",
      "content": "# agent.py\n\nimport openai\n\nclass AGIAgent:\n    def __init__(self, api_key):\n        \"\"\"\n        Initializes the AGI agent with an OpenAI API key.\n\n        Args:\n            api_key (str): The OpenAI API key.\n        \"\"\"\n        openai.api_key = api_key\n        self.memory = []\n\n    def process_input(self, user_input):\n        \"\"\"\n        Processes user input and interacts with the OpenAI API.\n\n        Args:\n            user_input (str): The user's input text.\n\n        Returns:\n            str: The agent's response.\n        \"\"\"\n        # Append user input to memory\n        self.memory.append(user_input)\n\n        # Construct prompt using memory and user input\n        prompt = \"\\n\".join(self.memory) + \"\\nUser: \" + user_input + \"\\nAGI:\"\n\n        # Generate response using OpenAI API\n        response = openai.Completion.create(\n            engine=\"text-davinci-003\",  # Use a suitable OpenAI engine\n            prompt=prompt,\n            max_tokens=150,\n            temperature=0.7\n        )\n\n        # Extract and return the generated text\n        return response.choices[0].text.strip()\n\n# Example usage:\n\nagent = AGIAgent(\"YOUR_API_KEY\")\nwhile True:\n    user_input = input(\"You: \")\n    response = agent.process_input(user_input)\n    print(\"AGI: \" + response)"
    }
  ]
}
```
