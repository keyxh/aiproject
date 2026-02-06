# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\nfrom typing import Optional\n\n# API Key for OpenAI, replace with your own\nAPI_KEY = 'your-api-key'\n\n# Initialize OpenAI client\nopenai.api_key = API_KEY\n\n\n\nclass AGI:\n    def __init__(self, model_name: str = 'gpt-3.5-turbo'):\n        self.model_name = model_name\n\n    def think(self, prompt: str, max_tokens: int = 50) -> Optional[str]:\n        \n        # Ensure that the prompt is not empty\n        if not prompt:\n            return None\n\n        # Call OpenAI API with the prompt\n        response = openai.Completion.create(\n            engine=self.model_name,\n            prompt=prompt,\n            max_tokens=max_tokens\n        )\n\n        # Return the response text from OpenAI\n        return response.choices[0].text.strip()\n\n\n\n# Example usage of the AGI class\nif __name__ == '__main__':\n    # Create an instance of AGI\n    agi_instance = AGI()\n\n    # Think and get a response to a prompt\n    prompt = 'Tell me a joke.'\n    response = agi_instance.think(prompt)\n\n    # Print the response\n    print(response)\n"
        }
    ]
}
```