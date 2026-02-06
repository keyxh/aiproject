# agi

```json
{
  "files": [
    {
      "filename": "agi.py",
      "content": "
import os
import json
import requests

class AGI:
  def __init__(self, api_key):
    self.api_key = api_key
    self.api_url = 'https://api.openai.com/v1'

  def get_response(self, prompt):
    headers = {
      'Authorization': f'Bearer {self.api_key}',
      'Content-Type': 'application/json'
    }
    data = {
      'prompt': prompt,
      'max_tokens': 1024,
      'temperature': 0.7
    }
    response = requests.post(f'{self.api_url}/completions', headers=headers, data=json.dumps(data))
    return response.json()['choices'][0]['text']

  def converse(self, prompt):
    response = self.get_response(prompt)
    return response

def main():
  api_key = os.environ.get('OPENAI_API_KEY')
  agi = AGI(api_key)
  while True:
    prompt = input('User: ')
    response = agi.converse(prompt)
    print('AGI:', response)

if __name__ == '__main__':
  main()
"
    }
  ]
}
```