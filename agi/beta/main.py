import openai
import os

# 配置OpenAI API密钥
openai.api_key = os.getenv('OPENAI_API_KEY')

if not openai.api_key:
    raise ValueError("OPENAI_API_KEY 环境变量未设置，请配置后重试")

# 简单的AGI交互函数
def agi_query(prompt: str) -> str:
    """
    使用OpenAI API生成对用户提示的响应
    :param prompt: 用户输入的提示
    :return: 模型生成的响应文本
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 使用最新模型，可替换为gpt-3.5-turbo等
            messages=[
                {"role": "system", "content": "你是一个具有通用智能的AI助手，能够回答各种问题并进行创造性思考。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"请求失败: {str(e)}"

# 主程序入口
if __name__ == "__main__":
    print("欢迎使用AGI系统！输入 'quit' 退出。")
    while True:
        user_input = input("用户: ")
        if user_input.lower() == 'quit':
            print("再见！")
            break
        response = agi_query(user_input)
        print(f"AGI: {response}")