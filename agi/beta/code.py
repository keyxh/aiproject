# agi

```json
{
    "files": [
        {
            "filename": "main.py",
            "content": "# This is a very basic example of interacting with the OpenAI API\n\nimport openai\n\n# Set your OpenAI API key\nopenai.api_key = \"YOUR_API_KEY\"\n\n# Example prompt\nprompt = \"What is the meaning of life?\"\n\n# Call the OpenAI API\nresponse = openai.Completion.create(\n  engine=\"text-davinci-003\",\n  prompt=prompt,\n  max_tokens=100,\n  temperature=0.7\n)\n\n# Print the response\nprint(response.choices[0].text.strip())"
        }
    ]
}
```
