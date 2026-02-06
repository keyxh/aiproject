# agi

```json
{
    "files": [
        {
            "filename": "main.py",
            "content": "# This is a basic example of interacting with the OpenAI API\n\nimport openai\n\n# Set your OpenAI API key\nopenai.api_key = \"YOUR_API_KEY\"\n\n# Define the prompt\nprompt = \"Translate 'Hello, world!' into French.\"\n\n# Call the OpenAI API\nresponse = openai.Completion.create(\n  engine=\"text-davinci-003\",\n  prompt=prompt,\n  max_tokens=60,\n  n=1,\n  stop=None,\n  temperature=0.7\n)\n\n# Print the response\nprint(response.choices[0].text.strip())"
        }
    ]
}
```
