import openai
import os
from typing import List, Dict, Any

# 配置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = "your_api_key_here"  # 请替换为你的实际API密钥

# 初始化OpenAI客户端
openai.api_key = os.getenv("OPENAI_API_KEY")

class AGIEngine:
    """
    AGI引擎核心类，用于模拟通用人工智能行为。
    当前版本基于OpenAI API实现基础对话与推理能力。
    """
    def __init__(self):
        self.conversation_history: List[Dict[str, Any]] = []
        self.system_prompt = "You are an AGI assistant capable of reasoning, learning, and adapting to any task. Respond with clarity, creativity, and depth."

    def add_message(self, role: str, content: str):
        """
        添加一条对话消息到历史记录中。
        :param role: 'user' 或 'assistant'
        :param content: 消息内容
        """
        self.conversation_history.append({"role": role, "content": content})

    def generate_response(self, user_input: str) -> str:
        """
        根据用户输入生成响应，调用OpenAI API。
        :param user_input: 用户输入内容
        :return: AI生成的响应文本
        """
        # 添加用户消息到历史
        self.add_message("user", user_input)

        # 构建对话上下文
        messages = [
            {"role": "system", "content": self.system_prompt}
        ] + self.conversation_history

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # 或者使用 "gpt-3.5-turbo" 以节省成本
                messages=messages,
                temperature=0.7,
                max_tokens=1500
            )
            # 提取AI响应内容
            ai_response = response.choices[0].message.content
            # 添加AI响应到历史
            self.add_message("assistant", ai_response)
            return ai_response
        except Exception as e:
            return f"Error: {str(e)}"

    def reset_conversation(self):
        """
        重置对话历史，开始新的对话。
        """
        self.conversation_history = []

# 示例使用
if __name__ == "__main__":
    agi = AGIEngine()
    print("AGI引擎已启动。输入 'quit' 退出。")
    
    while True:
        user_input = input("用户: ")
        if user_input.lower() == "quit":
            print("再见！")
            break
        
        response = agi.generate_response(user_input)
        print(f"AGI: {response}")