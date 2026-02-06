# agi

```json
{
  "files": [
    {
      "filename": "agi.py",
      "content": """
import os
import json
from typing import Dict, List
import requests

class AGI:
  def __init__(self, api_key: str):
    self.api_key = api_key
    self.api_url = 'https://api.openai.com/v1'

  def get_response(self, prompt: str) -> str:
    """
    获取OpenAI API的响应
    """
    headers = {
      'Authorization': f'Bearer {self.api_key}',
      'Content-Type': 'application/json'
    }
    data = {
      'prompt': prompt,
      'max_tokens': 1024,
      'temperature': 0.7
    }
    response = requests.post(f'{self.api_url}/completions', headers=headers, json=data)
    return response.json()['choices'][0]['text']

  def process_input(self, input_text: str) -> str:
    """
    处理输入文本
    """
    # TODO: 实现输入文本的预处理
    return input_text

  def generate_response(self, input_text: str) -> str:
    """
    生成响应
    """
    processed_input = self.process_input(input_text)
    response = self.get_response(processed_input)
    return response

def main():
  api_key = os.environ['OPENAI_API_KEY']
  agi = AGI(api_key)
  while True:
    user_input = input('用户输入：')
    response = agi.generate_response(user_input)
    print('AGI响应：', response)

if __name__ == '__main__':
  main()
"""
    },
    {
      "filename": "requirements.txt",
      "content": """
requests
"""
    },
    {
      "filename": "README.md",
      "content": """
# AGI 项目
实现一个真正意义上的 AGI，如果使用的模型 API 用 OpenAI API。
"""
    }
  ]
}
```