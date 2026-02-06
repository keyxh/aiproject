import openai
import os
from typing import List, Dict, Any, Optional

# 配置 OpenAI API 密钥
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"  # 替换为你的实际 API 密钥

# 初始化 OpenAI 客户端
openai.api_key = os.getenv("OPENAI_API_KEY")

class AGIEngine:
    """
    AGI（通用人工智能）引擎核心类，封装与 OpenAI API 的交互，支持多轮对话、任务规划、自我反思等能力。
    """
    def __init__(self, model: str = "gpt-4", temperature: float = 0.7):
        self.model = model
        self.temperature = temperature
        self.conversation_history: List[Dict[str, Any]] = []

    def add_message(self, role: str, content: str):
        """
        向对话历史中添加一条消息。
        :param role: "user" 或 "assistant"
        :param content: 消息内容
        """
        self.conversation_history.append({"role": role, "content": content})

    def generate_response(self, prompt: str, max_tokens: int = 500) -> str:
        """
        使用 OpenAI API 生成响应。
        :param prompt: 输入提示
        :param max_tokens: 最大响应长度
        :return: 生成的响应文本
        """
        # 将当前对话历史添加到提示中
        messages = self.conversation_history + [{"role": "user", "content": prompt}]

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=max_tokens
            )
            response_text = response.choices[0].message.content.strip()
            self.add_message("assistant", response_text)
            return response_text
        except Exception as e:
            return f"Error: {str(e)}"

    def self_reflect(self, reflection_prompt: str) -> str:
        """
        调用模型进行自我反思，评估当前对话状态或任务完成度。
        :param reflection_prompt: 反思提示词
        :return: 反思结果
        """
        reflection_message = {"role": "user", "content": reflection_prompt}
        self.conversation_history.append(reflection_message)

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=0.3,  # 低温度以获得更稳定反思
                max_tokens=300
            )
            reflection_result = response.choices[0].message.content.strip()
            self.add_message("assistant", reflection_result)
            return reflection_result
        except Exception as e:
            return f"Reflection Error: {str(e)}"

    def plan_task(self, task_description: str) -> str:
        """
        根据任务描述生成执行计划。
        :param task_description: 任务描述
        :return: 任务计划
        """
        plan_prompt = f"\nYou are an AGI agent. Your task is to plan how to accomplish the following: {task_description}\nPlease provide a step-by-step plan in bullet points."
        return self.generate_response(plan_prompt)

    def execute_task(self, task_description: str) -> str:
        """
        执行任务并返回结果。
        :param task_description: 任务描述
        :return: 执行结果
        """
        plan = self.plan_task(task_description)
        self.add_message("assistant", plan)
        
        execution_prompt = f"\nExecute the following plan: {plan}\nProvide the final result."
        return self.generate_response(execution_prompt)

# 示例用法
if __name__ == "__main__":
    agi = AGIEngine(model="gpt-4", temperature=0.8)
    
    # 初始化对话
    agi.add_message("user", "Hello, I am an AGI agent. What can you do?")
    response = agi.generate_response("Tell me about yourself.")
    print("AGI Response:", response)
    
    # 执行任务
    task_result = agi.execute_task("Write a short poem about the future of AI.")
    print("Task Result:", task_result)
    
    # 自我反思
    reflection = agi.self_reflect("What did you learn from the last task? How can you improve?")
    print("Self-Reflection:", reflection)