# agi

```json
{
  "files": [
    {
      "filename": "main.py",
      "content": "# This is a basic example of interacting with the OpenAI API\n\nimport openai\n\n# Set your OpenAI API key\nopenai.api_key = \"YOUR_API_KEY\"\n\n# Define a function to get a response from the OpenAI API\ndef get_response(prompt):\n    response = openai.Completion.create(\n        engine=\"text-davinci-003\",  # Replace with your desired engine\n        prompt=prompt,\n        max_tokens=100  # Adjust as needed\n    )\n    return response.choices[0].text\n\n# Example usage:\nuser_input = input(\"You: \")\nresponse = get_response(user_input)\nprint(\"AGI: \" + response)\n"
    }
  ]
}
```
