import openai
import os

# 配置OpenAI API密钥
openai.api_key = os.getenv('OPENAI_API_KEY')

if not openai.api_key:
    raise ValueError("请设置OPENAI_API_KEY环境变量")

# 简单的AGI交互函数
def agi_query(prompt: str) -> str:
    """
    使用OpenAI API生成智能响应
    :param prompt: 用户输入的提示
    :return: 模型生成的响应
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 使用最新模型
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"请求失败: {str(e)}"

# 主程序入口
if __name__ == "__main__":
    print("欢迎使用AGI系统！输入'quit'退出。")
    while True:
        user_input = input("用户: ")
        if user_input.lower() == 'quit':
            print("再见！")
            break
        response = agi_query(user_input)
        print(f"AGI: {response}")