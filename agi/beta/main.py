import openai
import os
from typing import List, Dict, Any

# 配置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"  # 替换为你的实际API密钥

# 初始化OpenAI客户端
openai.api_key = os.getenv("OPENAI_API_KEY")

class AGIEngine:
    """
    AGI引擎核心类，封装与OpenAI API交互逻辑，支持多轮对话、上下文管理、任务规划等。
    """
    def __init__(self, model: str = "gpt-4", temperature: float = 0.7):
        self.model = model
        self.temperature = temperature
        self.context_history: List[Dict[str, Any]] = []  # 用于存储对话历史

    def add_message(self, role: str, content: str):
        """
        添加一条消息到上下文历史中。
        :param role: 消息角色，如 'user' 或 'assistant'
        :param content: 消息内容
        """
        self.context_history.append({"role": role, "content": content})

    def generate_response(self, prompt: str, max_tokens: int = 200) -> str:
        """
        使用OpenAI API生成响应。
        :param prompt: 输入提示词
        :param max_tokens: 最大生成令牌数
        :return: 生成的响应文本
        """
        # 将当前提示词添加到上下文
        self.add_message("user", prompt)

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.context_history,
                temperature=self.temperature,
                max_tokens=max_tokens
            )
            # 提取响应内容
            response_text = response.choices[0].message.content.strip()
            # 将AI响应添加到上下文
            self.add_message("assistant", response_text)
            return response_text
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Error: Failed to generate response."

    def reset_context(self):
        """
        重置对话上下文历史。
        """
        self.context_history = []

    def get_context_length(self) -> int:
        """
        获取当前上下文历史中的消息数量。
        :return: 消息数量
        """
        return len(self.context_history)


# 示例使用
if __name__ == "__main__":
    # 初始化AGI引擎
    agi = AGIEngine(model="gpt-4", temperature=0.7)

    # 与AGI交互
    print("AGI: 你好！我是你的AGI助手。你可以问我任何问题。")
    while True:
        user_input = input("你：")
        if user_input.lower() in ["退出", "quit", "exit"]:
            print("AGI: 再见！")
            break
        
        response = agi.generate_response(user_input)
        print(f"AGI：{response}")

        # 可选：打印当前上下文长度
        # print(f"当前对话轮数：{agi.get_context_length()}轮")