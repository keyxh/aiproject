import openai
import os
import logging
from typing import List, Dict, Any, Optional

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 从环境变量加载OpenAI API密钥
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY 环境变量未设置")

# 初始化OpenAI客户端
openai.api_key = OPENAI_API_KEY

class AGIEngine:
    """
    AGI引擎核心类，负责与OpenAI API交互，模拟通用人工智能行为。
    支持多轮对话、上下文记忆、任务分解与自我反思。
    """
    def __init__(self, model: str = "gpt-4", max_tokens: int = 2048):
        self.model = model
        self.max_tokens = max_tokens
        self.conversation_history: List[Dict[str, Any]] = []
        self.system_prompt = "你是一个通用人工智能助手，能够理解并执行复杂任务。请以清晰、有逻辑的方式回答问题，并在必要时进行自我反思和任务分解。"

    def add_system_prompt(self, prompt: str):
        """
        设置系统提示词，用于引导AI行为。
        """
        self.system_prompt = prompt

    def add_message(self, role: str, content: str):
        """
        添加一条对话消息到历史记录中。
        """
        self.conversation_history.append({"role": role, "content": content})

    def get_response(self, user_input: str, temperature: float = 0.7) -> str:
        """
        从用户输入生成响应。
        :param user_input: 用户输入内容
        :param temperature: 控制生成的随机性，0.0~1.0
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
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=temperature
            )
            reply = response.choices[0].message.content
            self.add_message("assistant", reply)
            logger.info(f"生成回复: {reply[:100]}...")
            return reply
        except Exception as e:
            logger.error(f"调用OpenAI API失败: {e}")
            return "抱歉，我无法处理该请求。"

    def self_reflect(self, context: str) -> str:
        """
        自我反思方法，用于评估当前任务执行情况并提出改进。
        """
        prompt = f"请反思以下上下文：{context}。你是否完成了任务？如果有不足，请提出改进方案。"
        return self.get_response(prompt, temperature=0.8)

    def task_decompose(self, task: str) -> List[str]:
        """
        将复杂任务分解为多个子任务。
        :param task: 待分解的任务描述
        :return: 子任务列表
        """
        prompt = f"请将以下任务分解为多个可执行的子任务：{task}。请以列表形式返回，每个子任务用数字编号。"
        response = self.get_response(prompt, temperature=0.5)
        # 简单解析响应，实际项目中应使用更健壮的解析器
        lines = response.split('\n')
        subtasks = []
        for line in lines:
            if line.strip().startswith(('1.', '2.', '3.', '4.', '5.')):
                subtasks.append(line.strip())
        return subtasks

    def reset_conversation(self):
        """
        重置对话历史。
        """
        self.conversation_history = []

# 示例使用
if __name__ == "__main__":
    # 初始化AGI引擎
    agi = AGIEngine(model="gpt-4", max_tokens=1500)
    
    # 设置系统提示
    agi.add_system_prompt("你是一个具备逻辑推理和自我学习能力的通用人工智能助手。")
    
    # 与用户交互
    print("欢迎使用AGI助手！输入'quit'退出。")
    while True:
        user_input = input("用户: ")
        if user_input.lower() == "quit":
            break
        
        response = agi.get_response(user_input)
        print(f"AGI: {response}")
        
        # 可选：自我反思
        # reflect = agi.self_reflect(f"用户输入: {user_input}\nAI响应: {response}")
        # print(f"反思: {reflect}")