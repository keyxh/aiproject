# agi

```json
{
  "files": [
    {
      "filename": "agi.py",
      "content": "# agi.py\n\nimport openai\n\n# Set your OpenAI API key\nopenai.api_key = \"YOUR_API_KEY\"\n\nclass AGI:\n    def __init__(self):\n        self.memory = []\n\n    def process_input(self, input_text):\n        \"\"\"\n        Processes user input and generates a response.\n\n        Args:\n            input_text (str): The user's input text.\n\n        Returns:\n            str: The generated response.\n        \"\"\"\n\n        # Append input to memory\n        self.memory.append(input_text)\n\n        # Construct the prompt for the OpenAI API\n        prompt = \"\\n\".join(self.memory) + \"\\nUser: \" + input_text + \"\\nAGI:\"\n\n        # Generate response using OpenAI API\n        response = openai.Completion.create(\n            engine=\"text-davinci-003\",  # Use a suitable OpenAI model\n            prompt=prompt,\n            max_tokens=100,\n            temperature=0.7\n        )\n\n        return response.choices[0].text\n\n# Example usage\n agi = AGI()\n while True:\n     user_input = input(\"You: \")\n     if user_input.lower() == \"exit\":\n         break\n     response = agi.process_input(user_input)\n     print(\"AGI: \" + response)"
    }
  ]
}
```
