# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\nfrom flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n# API Key for OpenAI - This should be stored securely and not hardcoded in production\nopenai.api_key = 'your_openai_api_key'\n\n\n# Function to generate responses using OpenAI's GPT-3 model\ndef generate_response(prompt):\n    response = openai.Completion.create(\n        engine='text-davinci-002',\n        prompt=prompt,\n        max_tokens=150\n    )\n    return response.choices[0].text.strip()\n\n\n# Route to handle incoming requests and generate responses\n@app.route('/generate', methods=['POST'])\ndef handle_request):\n    data = request.get_json()\n    if 'prompt' not in data:\n        return jsonify({'error': 'Missing prompt in request'}), 400\n    prompt = data['prompt']\n    response = generate_response(prompt)\n    return jsonify({'response': response})\n\nif __name__ == '__main__':\n    app.run(debug=True)\n"
        },
        {
            "filename": "requirements.txt",
            "content": "Flask==2.0.3\nopenai==0.27.0\n"
        },
        {
            "filename": "README.md",
            "content": "# AGI Project\n\nThis repository contains the source code for the 'agi' project, which utilizes the OpenAI API to create a general AI capable of generating responses to various prompts.\n\n## Setup\n\n1. Clone the repository:\n    git clone https://github.com/yourusername/agi.git\n\n2. Navigate to the project directory:\n    cd agi\n\n3. Install the required packages:\n    pip install -r requirements.txt\n\n4. Set your OpenAI API key in the 'agi.py' file under the 'openai.api_key' line.\n\n## Usage\n\nTo generate a response, send a POST request to the '/generate' endpoint with a JSON payload containing the 'prompt' field.\n\nExample request:\n\n    POST /generate\n    Content-Type: application/json\n\n    {\n        \"prompt\": \"What is the capital of France?\"\n    }\n\nExample response:\n\n    {\n        \"response\": \"The capital of France is Paris.\"\n    }\n"
        }
    ]
}
```