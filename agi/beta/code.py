# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "import openai

# 初始化OpenAI API客户端
openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_response(user_input):
    # 使用OpenAI的ChatCompletion函数来生成响应
    response = openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=[
            {"role": "user", "content": user_input},
        ],
        temperature=0.7,
    )
    # 返回生成的响应文本
    return response.choices[0].message.content

if __name__ == '__main__':
    user_input = input('你: ')
    response = generate_response(user_input)
    print('AGI: ', response)"
        }
    ]
}
```