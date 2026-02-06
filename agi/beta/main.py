import openai
import os
from typing import List, Dict, Any, Optional

# 配置 OpenAI API 密钥
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"  # 请替换为实际密钥

# 初始化 OpenAI 客户端
openai.api_key = os.getenv("OPENAI_API_KEY")

class AGIEngine:
    """
    AGI 引擎核心类，封装与 OpenAI API 的交互，支持多轮对话、上下文管理、任务规划等。
    """
    def __init__(self, model: str = "gpt-4", temperature: float = 0.7):
        self.model = model
        self.temperature = temperature
        self.context_history: List[Dict[str, Any]] = []  # 存储对话历史

    def add_message(self, role: str, content: str):
        """
        添加一条消息到上下文历史中。
        role: "user" 或 "assistant"
        """
        self.context_history.append({"role": role, "content": content})

    def get_response(self, prompt: str, max_tokens: int = 500) -> str:
        """
        从 OpenAI 获取响应。
        prompt: 用户输入的提示词
        """
        # 添加当前提示到上下文
        self.add_message("user", prompt)

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.context_history,
                temperature=self.temperature,
                max_tokens=max_tokens
            )
            # 提取回复内容
            reply = response.choices[0].message.content
            self.add_message("assistant", reply)
            return reply
        except Exception as e:
            return f"Error: {str(e)}"

    def reset_context(self):
        """
        重置对话上下文历史。
        """
        self.context_history = []

    def plan_task(self, task_description: str) -> str:
        """
        根据任务描述生成执行计划。
        """
        prompt = f"你是一个 AGI 系统。请为以下任务生成一个分步骤的执行计划：\n\n{task_description}\n\n请以清晰的步骤列出如何完成该任务。"
        return self.get_response(prompt)

    def reflect_and_improve(self, current_output: str, feedback: str) -> str:
        """
        根据反馈反思并改进当前输出。
        """
        prompt = f"你是一个 AGI 系统。你之前输出了以下内容：\n\n{current_output}\n\n现在收到以下反馈：\n\n{feedback}\n\n请根据反馈改进你的输出。"
        return self.get_response(prompt)

# 示例使用
if __name__ == "__main__":
    agi = AGIEngine(model="gpt-4", temperature=0.8)
    
    # 示例任务
    task = "编写一个 Python 脚本，从 API 获取数据并保存为 CSV 文件。"
    plan = agi.plan_task(task)
    print("任务计划：\n", plan)
    
    # 模拟用户反馈
    feedback = "请在脚本中加入错误处理和日志记录。"
    improved = agi.reflect_and_improve(plan, feedback)
    print("改进后的计划：\n", improved)
    
    # 重置上下文
    agi.reset_context()
    print("上下文已重置。")