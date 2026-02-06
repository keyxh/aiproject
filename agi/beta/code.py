# agi

```json
{
  "files": [
    {
      "filename": "agi.py",
      "content": "
# AGI 项目实现
# 作者：初级工程师
# 日期：2023-02-20

import os
import json
import requests

# OpenAI API 设置
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
OPENAI_API_URL = 'https://api.openai.com/v1/'

# AGI 类定义
class AGI:
  def __init__(self, api_key):
    self.api_key = api_key

  # 获取 OpenAI API 的回答
  def get_answer(self, question):
    headers = {
      'Authorization': f'Bearer {self.api_key}',
      'Content-Type': 'application/json'
    }
    data = {
      'prompt': question,
      'max_tokens': 1024,
      'temperature': 0.7
    }
    response = requests.post(OPENAI_API_URL + 'completions', headers=headers, json=data)
    return response.json()['choices'][0]['text']

  # 处理用户输入
  def handle_input(self, input_text):
    answer = self.get_answer(input_text)
    return answer

# 主函数
def main():
  agi = AGI(OPENAI_API_KEY)
  while True:
    user_input = input('用户输入：')
    answer = agi.handle_input(user_input)
    print('AGI 回答：', answer)

if __name__ == '__main__':
  main()
"
    },
    {
      "filename": "requirements.txt",
      "content": "
requests
"
    }
  ]
}
```