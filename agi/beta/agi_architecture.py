import os
import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
import openai

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class AGIConfig:
    """AGI系统配置类"""
    openai_api_key: str
    model_name: str = "gpt-4"
    temperature: float = 0.7
    max_tokens: int = 2000
    memory_window_size: int = 10


class MemoryModule(ABC):
    """记忆模块抽象基类"""
    
    @abstractmethod
    def store(self, content: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        pass
    
    @abstractmethod
    def retrieve(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        pass
    
    @abstractmethod
    def clear(self) -> None:
        pass


class ShortTermMemory(MemoryModule):
    """短期记忆实现 - 基于对话历史"""
    
    def __init__(self, window_size: int = 10):
        self.window_size = window_size
        self.history: List[Dict[str, str]] = []
    
    def store(self, content: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        role = metadata.get("role", "user") if metadata else "user"
        self.history.append({"role": role, "content": content})
        # 保持窗口大小
        if len(self.history) > self.window_size:
            self.history.pop(0)
    
    def retrieve(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        return self.history[-limit:] if self.history else []
    
    def clear(self) -> None:
        self.history.clear()


class ReasoningEngine(ABC):
    """推理引擎抽象基类"""
    
    @abstractmethod
    def process(self, input_text: str, context: List[Dict[str, str]]) -> str:
        pass


class OpenAIReasoningEngine(ReasoningEngine):
    """基于OpenAI API的推理引擎"""
    
    def __init__(self, config: AGIConfig):
        self.config = config
        openai.api_key = config.openai_api_key
    
    def process(self, input_text: str, context: List[Dict[str, str]]) -> str:
        try:
            messages = context + [{"role": "user", "content": input_text}]
            response = openai.ChatCompletion.create(
                model=self.config.model_name,
                messages=messages,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens
            )
            return response.choices[0].message["content"].strip()
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            raise


class AGICore:
    """AGI核心系统"""
    
    def __init__(self, config: AGIConfig):
        self.config = config
        self.memory = ShortTermMemory(window_size=config.memory_window_size)
        self.reasoning_engine = OpenAIReasoningEngine(config)
    
    def process_input(self, user_input: str) -> str:
        """处理用户输入并返回响应"""
        # 从记忆中检索上下文
        context = self.memory.retrieve(user_input)
        
        # 使用推理引擎处理
        response = self.reasoning_engine.process(user_input, context)
        
        # 存储交互到记忆
        self.memory.store(user_input, {"role": "user"})
        self.memory.store(response, {"role": "assistant"})
        
        return response
    
    def reset_memory(self) -> None:
        """重置记忆"""
        self.memory.clear()


def create_agi_system() -> AGICore:
    """工厂函数：创建AGI系统实例"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is required")
    
    config = AGIConfig(
        openai_api_key=api_key,
        model_name=os.getenv("AGI_MODEL_NAME", "gpt-4"),
        temperature=float(os.getenv("AGI_TEMPERATURE", "0.7")),
        max_tokens=int(os.getenv("AGI_MAX_TOKENS", "2000")),
        memory_window_size=int(os.getenv("AGI_MEMORY_WINDOW", "10"))
    )
    
    return AGICore(config)


# 使用示例
if __name__ == "__main__":
    # 确保设置了OPENAI_API_KEY环境变量
    try:
        agi = create_agi_system()
        
        # 简单交互循环
        print("AGI系统已启动。输入'quit'退出。")
        while True:
            user_input = input("\n用户: ")
            if user_input.lower() in ['quit', 'exit']:
                break
            
            response = agi.process_input(user_input)
            print(f"AGI: {response}")
            
    except Exception as e:
        logger.error(f"AGI系统错误: {e}")