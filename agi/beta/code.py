# agi

<think>The user is asking me to generate code for an AGI (Artificial General Intelligence) project called "agi" using OpenAI API. They want me to act as a senior engineer and generate practical, runnable code with best practices, comments, and documentation.

The output should be in JSON format with files containing filenames and content.

Let me think about what would be appropriate for an AGI project. Since we're talking about "true AGI" but using OpenAI API, I should create a framework that:
1. Provides a modular architecture for AGI development
2. Uses OpenAI's API as the core intelligence
3. Implements key AGI components like:
   - Memory system (short-term and long-term)
   - Planning and reasoning
   - Learning capabilities
   - Tool use
   - Self-reflection
4. Follows best practices with proper error handling, logging, etc.

I'll create a comprehensive but practical implementation that could serve as a foundation for AGI development. Let me structure this properly:

1. Main AGI core class
2. Memory management system
3. Planning and reasoning module
4. Tool/function calling system
5. Configuration management
6. Main entry point

Let me write the code in Chinese as requested, with comprehensive documentation.
</think>

```json
{
    "files": [
        {
            "filename": "agi/config.py",
            "content": "\"\"\"\nAGI 项目配置模块\n\n提供统一的配置管理，支持环境变量和配置文件两种方式。\n\"\"\"\n\nimport os\nfrom dataclasses import dataclass, field\nfrom typing import Optional\nfrom pathlib import Path\n\n\n@dataclass\nclass OpenAIConfig:\n    \"\"\"OpenAI API 配置\"\"\"\n    api_key: str = field(default_factory=lambda: os.getenv(\"OPENAI_API_KEY\", \"\"))\n    base_url: str = field(default_factory=lambda: os.getenv(\"OPENAI_BASE_URL\", \"https://api.openai.com/v1\"))\n    model: str = field(default_factory=lambda: os.getenv(\"OPENAI_MODEL\", \"gpt-4\"))\n    max_tokens: int = field(default_factory=lambda: int(os.getenv(\"OPENAI_MAX_TOKENS\", \"4096\")))\n    temperature: float = field(default_factory=lambda: float(os.getenv(\"OPENAI_TEMPERATURE\", \"0.7\")))\n    timeout: int = field(default_factory=lambda: int(os.getenv(\"OPENAI_TIMEOUT\", \"60\")))\n    \n    def validate(self) -> bool:\n        \"\"\"验证配置是否有效\"\"\"\n        if not self.api_key:\n            raise ValueError(\"OpenAI API key 未设置，请设置 OPENAI_API_KEY 环境变量\")\n        return True\n\n\n@dataclass\nclass MemoryConfig:\n    \"\"\"记忆系统配置\"\"\"\n    short_term_capacity: int = field(default_factory=lambda: int(os.getenv(\"SHORT_TERM_CAPACITY\", \"10\")))\n    long_term_storage_path: str = field(default_factory=lambda: os.getenv(\"LONG_TERM_STORAGE_PATH\", \"./memory\"))\n    embedding_model: str = field(default_factory=lambda: os.getenv(\"EMBEDDING_MODEL\", \"text-embedding-ada-002\"))\n    \n    def validate(self) -> bool:\n        \"\"\"验证配置\"\"\"\n        Path(self.long_term_storage_path).mkdir(parents=True, exist_ok=True)\n        return True\n\n\n@dataclass\nclass AGIConfig:\n    \"\"\"AGI 系统主配置\"\"\"\n    openai: OpenAIConfig = field(default_factory=OpenAIConfig)\n    memory: MemoryConfig = field(default_factory=MemoryConfig)\n    debug_mode: bool = field(default_factory=lambda: os.getenv(\"DEBUG_MODE\", \"false\").lower() == \"true\")\n    max_iterations: int = field(default_factory=lambda: int(os.getenv(\"MAX_ITERATIONS\", \"10\")))\n    \n    def validate(self) -> bool:\n        \"\"\"验证所有配置\"\"\"\n        self.openai.validate()\n        self.memory.validate()\n        return True\n\n\ndef load_config(config_path: Optional[str] = None) -> AGIConfig:\n    \"\"\"\n    加载配置\n    \n    Args:\n        config_path: 配置文件路径，支持 .env 或 YAML 格式\n        \n    Returns:\n        AGIConfig: 配置对象\n    \"\"\"\n    config = AGIConfig()\n    \n    # 如果提供了配置文件路径，可以在这里加载\n    if config_path:\n        # TODO: 实现配置文件加载逻辑\n        pass\n    \n    return config\n"
        },
        {
            "filename": "agi/memory.py",
            "content": "\"\"\"\nAGI 记忆系统模块\n\n实现分层的记忆系统：\n1. 工作记忆（Working Memory）：短期记忆，存储当前对话上下文\n2. 情景记忆（Episodic Memory）：存储具体的经历和事件\n3. 语义记忆（Semantic Memory）：存储抽象知识和事实\n4. 程序记忆（Procedural Memory）：存储技能和习惯\n\"\"\"\n\nimport json\nimport uuid\nimport time\nfrom datetime import datetime\nfrom typing import List, Dict, Optional, Any\nfrom dataclasses import dataclass, field, asdict\nfrom pathlib import Path\nfrom abc import ABC, abstractmethod\nimport logging\n\nlogger = logging.getLogger(__name__)\n\n\n@dataclass\nclass Memory:\n    \"\"\"记忆基础数据结构\"\"\"\n    id: str = field(default_factory=lambda: str(uuid.uuid4()))\n    content: str = \"\"\n    memory_type: str = \"semantic\"  # semantic, episodic, procedural, working\n    importance: float = 0.5  # 0-1, 重要性评分\n    created_at: float = field(default_factory=time.time)\n    last_accessed: float = field(default_factory=time.time)\n    access_count: int = 0\n    metadata: Dict[str, Any] = field(default_factory=dict)\n    embedding: Optional[List[float]] = None\n    \n    def access(self):\n        \"\"\"访问记忆\"\"\"\n        self.last_accessed = time.time()\n        self.access_count += 1\n    \n    def to_dict(self) -> Dict:\n        \"\"\"转换为字典\"\"\"\n        return asdict(self)\n    \n    @classmethod\n    def from_dict(cls, data: Dict) -> 'Memory':\n        \"\"\"从字典创建记忆\"\"\"\n        return cls(**data)\n\n\nclass MemoryStore(ABC):\n    \"\"\"记忆存储抽象基类\"\"\"\n    \n    @abstractmethod\n    def add(self, memory: Memory) -> bool:\n        \"\"\"添加记忆\"\"\"\n        pass\n    \n    @abstractmethod\n    def get(self, memory_id: str) -> Optional[Memory]:\n        \"\"\"获取记忆\"\"\"\n        pass\n    \n    @abstractmethod\n    def search(self, query: str, limit: int = 5) -> List[Memory]:\n        \"\"\"搜索记忆\"\"\"\n        pass\n    \n    @abstractmethod\n    def remove(self, memory_id: str) -> bool:\n        \"\"\"删除记忆\"\"\"\n        pass\n\n\nclass WorkingMemoryStore(MemoryStore):\n    \"\"\"工作记忆存储 - 基于队列的短期记忆\"\"\"\n    \n    def __init__(self, capacity: int = 10):\n        self.capacity = capacity\n        self.memories: List[Memory] = []\n    \n    def add(self, memory: Memory) -> bool:\n        \"\"\"添加工作记忆，超出容量时移除最旧的\"\"\"\n        memory.memory_type = \"working\"\n        self.memories.append(memory)\n        \n        # 保持容量限制\n        while len(self.memories) > self.capacity:\n            removed = self.memories.pop(0)\n            logger.debug(f\"工作记忆已满，移除记忆: {removed.id}\")\n        \n        return True\n    \n    def get(self, memory_id: str) -> Optional[Memory]:\n        for memory in self.memories:\n            if memory.id == memory_id:\n                memory.access()\n                return memory\n        return None\n    \n    def search(self, query: str, limit: int = 5) -> List[Memory]:\n        \"\"\"简单关键词搜索\"\"\"\n        results = []\n        for memory in self.memories:\n            if query.lower() in memory.content.lower():\n                memory.access()\n                results.append(memory)\n                if len(results) >= limit:\n                    break\n        return results\n    \n    def remove(self, memory_id: str) -> bool:\n        for i, memory in enumerate(self.memories):\n            if memory.id == memory_id:\n                self.memories.pop(i)\n                return True\n        return False\n    \n    def get_all(self) -> List[Memory]:\n        \"\"\"获取所有工作记忆\"\"\"\n        return self.memories.copy()\n    \n    def clear(self):\n        \"\"