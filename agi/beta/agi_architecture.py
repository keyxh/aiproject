import os
import json
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from dataclasses import dataclass
from openai import OpenAI


class AGIComponent(ABC):
    """抽象基类，定义AGI系统中所有组件的通用接口。"""
    
    @abstractmethod
    def process(self, input_data: Any) -> Any:
        pass


@dataclass
class AGIConfig:
    """AGI系统的配置数据类。"""
    openai_api_key: str
    model_name: str = "gpt-4o"
    max_tokens: int = 1024
    temperature: float = 0.7
    memory_enabled: bool = True
    reasoning_enabled: bool = True


class MemoryModule(AGIComponent):
    """记忆模块：负责短期和长期记忆管理。"""
    
    def __init__(self):
        self.short_term_memory: List[Dict] = []
        self.long_term_memory: Dict[str, Any] = {}
    
    def store(self, key: str, value: Any, memory_type: str = "short"):
        if memory_type == "short":
            self.short_term_memory.append({"key": key, "value": value})
        elif memory_type == "long":
            self.long_term_memory[key] = value
    
    def retrieve(self, key: str, memory_type: str = "short") -> Optional[Any]:
        if memory_type == "short":
            for item in reversed(self.short_term_memory):
                if item["key"] == key:
                    return item["value"]
        elif memory_type == "long" and key in self.long_term_memory:
            return self.long_term_memory[key]
        return None
    
    def process(self, input_data: Any) -> Any:
        # 此处可扩展为自动记忆提取逻辑
        return input_data


class ReasoningModule(AGIComponent):
    """推理模块：基于输入和记忆进行逻辑推理。"""
    
    def __init__(self, client: OpenAI, config: AGIConfig):
        self.client = client
        self.config = config
    
    def process(self, input_data: Dict[str, Any]) -> str:
        prompt = f"""
        You are an advanced reasoning engine.
        Context: {input_data.get('context', '')}
        Task: {input_data.get('task', '')}
        Previous interactions: {input_data.get('history', [])}
        Provide a clear, step-by-step reasoning to solve the task.
        """
        
        response = self.client.chat.completions.create(
            model=self.config.model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature
        )
        return response.choices[0].message.content.strip()


class ActionModule(AGIComponent):
    """行动模块：将推理结果转化为具体行动或输出。"""
    
    def __init__(self, client: OpenAI, config: AGIConfig):
        self.client = client
        self.config = config
    
    def process(self, reasoning_output: str) -> str:
        prompt = f"""
        Based on the following reasoning, generate a concise and actionable response:
        {reasoning_output}
        """
        
        response = self.client.chat.completions.create(
            model=self.config.model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature
        )
        return response.choices[0].message.content.strip()


class AGICore:
    """AGI核心协调器，整合各模块形成统一系统。"""
    
    def __init__(self, config: AGIConfig):
        self.config = config
        self.client = OpenAI(api_key=config.openai_api_key)
        
        self.memory = MemoryModule() if config.memory_enabled else None
        self.reasoner = ReasoningModule(self.client, config) if config.reasoning_enabled else None
        self.action_module = ActionModule(self.client, config)
        
        self.conversation_history: List[Dict] = []
    
    def interact(self, user_input: str) -> str:
        # 存储用户输入到短期记忆
        if self.memory:
            self.memory.store("user_input", user_input, "short")
            self.conversation_history.append({"role": "user", "content": user_input})
        
        # 构建推理输入
        reasoning_input = {
            "task": user_input,
            "context": "",
            "history": self.conversation_history[-5:] if len(self.conversation_history) > 5 else self.conversation_history
        }
        
        # 推理
        if self.reasoner:
            reasoning_result = self.reasoner.process(reasoning_input)
        else:
            reasoning_result = user_input  # 直通模式
        
        # 行动（生成最终响应）
        final_response = self.action_module.process(reasoning_result)
        
        # 存储AI响应
        if self.memory:
            self.memory.store("ai_response", final_response, "short")
            self.conversation_history.append({"role": "assistant", "content": final_response})
        
        return final_response


def main():
    """示例主函数，展示如何初始化和使用AGI系统。"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("请设置环境变量 OPENAI_API_KEY")
    
    config = AGIConfig(openai_api_key=api_key)
    agi = AGICore(config)
    
    print("AGI系统已启动。输入 'quit' 退出。")
    while True:
        user_input = input("你: ")
        if user_input.lower() == "quit":
            break
        response = agi.interact(user_input)
        print(f"AGI: {response}")


if __name__ == "__main__":
    main()
