import openai
import os
from typing import List, Dict, Any

# 配置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"  # 替换为你的实际API密钥

# 初始化OpenAI客户端
openai.api_key = os.getenv("OPENAI_API_KEY")

class AGIEngine:
    """
    AGI引擎核心类，封装与OpenAI API交互逻辑，支持多轮对话、上下文管理、任务分解等。
    """
    def __init__(self, model: str = "gpt-4", temperature: float = 0.7):
        self.model = model
        self.temperature = temperature
        self.conversation_history: List[Dict[str, Any]] = []

    def add_message(self, role: str, content: str):
        """
        添加一条对话消息到历史记录中。
        :param role: "user" 或 "assistant"
        :param content: 消息内容
        """
        self.conversation_history.append({"role": role, "content": content})

    def get_response(self, prompt: str) -> str:
        """
        向OpenAI模型发送请求并获取响应。
        :param prompt: 用户输入或系统提示
        :return: 模型生成的响应文本
        """
        # 将历史对话添加到上下文中
        messages = self.conversation_history + [{"role": "user", "content": prompt}]

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=1500
            )
            reply = response.choices[0].message.content
            self.add_message("assistant", reply)
            return reply
        except Exception as e:
            return f"Error: {str(e)}"

    def reset_conversation(self):
        """
        重置对话历史。
        """
        self.conversation_history = []

    def set_system_prompt(self, system_prompt: str):
        """
        设置系统提示词，用于引导模型行为。
        :param system_prompt: 系统提示内容
        """
        self.conversation_history.insert(0, {"role": "system", "content": system_prompt})

# 示例使用
if __name__ == "__main__":
    # 初始化AGI引擎
    agi = AGIEngine(model="gpt-4", temperature=0.7)
    
    # 设置系统提示
    agi.set_system_prompt("你是一个具有深度思考能力的AGI助手，能够处理复杂任务并提供高质量解决方案。")
    
    # 与用户交互
    print("欢迎使用AGI助手！输入 'quit' 退出。")
    while True:
        user_input = input("用户: ")
        if user_input.lower() == "quit":
            print("再见！")
            break
        
        response = agi.get_response(user_input)
        print(f"AGI: {response}")