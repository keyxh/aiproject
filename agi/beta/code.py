# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\n\nclass AGI:\n    \n    def __init__(self, api_key):\n        \n        # Initialize the OpenAI client with the provided API key\n        self.client = openai.OpenAI(api_key=api_key)\n\n    \n    def think(self, prompt):\n        \n        # Generate a response using the OpenAI API\n        response = self.client.Completion.create(\n            engine=\"text-davinci-002\",\n            prompt=prompt,\n            max_tokens=150\n        )\n\n        # Return the generated text\n        return response.choices[0].text.strip()\n\n    \n    def ask_question(self, question):\n        \n        # Format the question to be a thinking prompt\n        prompt = f\"Question: {question}. Answer:\"\n\n        # Generate an answer using the OpenAI API\n        answer = self.think(prompt)\n\n        # Return the generated answer\n        return answer\n\n# Usage example:\nif __name__ == \"__main__\":\n    \n    # Replace 'your_api_key_here' with your actual OpenAI API key\n    api_key = 'your_api_key_here'\n\n    # Create an instance of AGI\n    agi_instance = AGI(api_key)\n\n    # Ask a question and get an answer\n    question = 'What is the capital of France?'\n    answer = agi_instance.ask_question(question)\n\n    # Print the answer\n    print(answer)\n"
        }
    ]
}
```