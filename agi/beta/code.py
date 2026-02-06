# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\nfrom flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n# Set your OpenAI API key here\nOPENAI_API_KEY = 'your-api-key'\nopenai.api_key = OPENAI_API_KEY\n\n\n# Function to call OpenAI API and generate response\ndef generate_response(prompt):\n    response = openai.Completion.create(\n        engine='text-davinci-002',\n        prompt=prompt,\n        max_tokens=150\n    )\n    return response.choices[0].text.strip()\n\n\n@app.route('/generate', methods=['POST'])\ndef generate_route):\n    data = request.get_json()\n    prompt = data.get('prompt', '')\n    if not prompt:\n        return jsonify({'error': 'No prompt provided'}), 400\n    response_text = generate_response(prompt)\n    return jsonify({'response': response_text})\n\nif __name__ == '__main__':\n    app.run(debug=True)\n"
        },
        {
            "filename": "README.md",
            "content": "# AGI Project\n\nThis project aims to create a true AGI using the OpenAI API.\n\n## Features\n- Uses OpenAI's GPT-3 model to generate responses.\n- A simple Flask web service to interact with the AGI.\n\n## Setup\n1. Install Python 3.8 or higher.\n2. Install Flask: `pip install Flask`\n3. Set your OpenAI API key in the `agi.py` file.\n4. Run the `agi.py` file using `python agi.py`.\n\n## Usage\nTo generate a response, send a POST request to the `/generate` endpoint with a JSON body containing the `prompt` field.\n\nExample:\n```json\n{\n    \"prompt\": \"Explain the concept of machine learning in simple terms.\"\n}\n```\n\nYou will receive a JSON response with the generated text in the `response` field.\n"
        }
    ]
}
```