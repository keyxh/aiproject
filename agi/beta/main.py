import openai
import os
from typing import List, Dict, Any

# 配置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"  # 请替换为你的实际API密钥

# 初始化OpenAI客户端
openai.api_key = os.getenv("OPENAI_API_KEY")

class AGIEngine:
    """
    AGI引擎核心类，封装与OpenAI API交互逻辑，支持多轮对话、上下文管理、任务规划等。
    """
    def __init__(self):
        self.context_history: List[Dict[str, Any]] = []  # 存储对话历史
        self.system_prompt = "你是一个具有自我学习和推理能力的通用人工智能助手。请根据用户需求提供准确、深入、有逻辑的回答。"

    def add_system_prompt(self, prompt: str):
        """
        设置系统提示词，用于引导AI行为。
        """
        self.system_prompt = prompt

    def generate_response(self, user_input: str) -> str:
        """
        根据用户输入生成响应。
        使用OpenAI API调用GPT模型，结合上下文历史。
        """
        # 构建对话上下文
        messages = [
            {"role": "system", "content": self.system_prompt}
        ] + self.context_history + [{"role": "user", "content": user_input}]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # 或者 "gpt-3.5-turbo"，根据需求调整
                messages=messages,
                temperature=0.7,
                max_tokens=1500
            )
            # 提取回复内容
            assistant_reply = response.choices[0].message.content
            
            # 更新上下文历史
            self.context_history.append({"role": "user", "content": user_input})
            self.context_history.append({"role": "assistant", "content": assistant_reply})
            
            return assistant_reply
        except Exception as e:
            return f"API调用失败: {str(e)}"

    def reset_context(self):
        """
        重置对话上下文，开始新的对话。
        """
        self.context_history = []

    def get_context_length(self) -> int:
        """
        获取当前上下文历史长度（用于调试或限制长度）。
        """
        return len(self.context_history)

# 示例使用
if __name__ == "__main__":
    agi = AGIEngine()
    agi.add_system_prompt("你是一个具备多领域知识的AI助手，能回答复杂问题并进行推理。")
    
    print("AGI引擎已启动。输入 'quit' 退出。")
    while True:
        user_input = input("用户: ")
        if user_input.lower() == "quit":
            print("再见！")
            break
        
        response = agi.generate_response(user_input)
        print(f"AGI: {response}")
        
        # 可选：打印当前上下文长度
        # print(f"当前上下文长度: {agi.get_context_length()}")