# agi

```json
{
  "files": [
    {
      "filename": "main.py",
      "content": "# This is a simple example of using OpenAI's API\nimport openai\n\n# Set your OpenAI API key\nopenai.api_key = \"YOUR_API_KEY\"\n\n# Define a function to interact with the OpenAI API\ndef ask_openai(prompt):\n    response = openai.Completion.create(\n        engine=\"text-davinci-003\",\n        prompt=prompt,\n        max_tokens=1024,\n        n=1,\n        stop=None,\n        temperature=0.7\n    )\n    return response.choices[0].text\n\n# Example usage\nuser_input = input(\"You: \")\nresponse = ask_openai(user_input)\nprint(\"AGI: \" + response)\n"
    }
  ]
}
```
