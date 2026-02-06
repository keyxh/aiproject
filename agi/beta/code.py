# agi

<think>The user is asking me to generate code for a project called "agi" (Artificial General Intelligence) as a junior engineer. The project description mentions implementing a true AGI using OpenAI API.

Let me analyze this request carefully:

1. **Writing Type**: This is a code generation task with a specific JSON output format
2. **Language**: The user wrote in Chinese, so I should respond in Chinese with the code itself in English (as code is typically written in English)
3. **Role**: Junior Engineer - so the code should be practical, well-commented, and follow best practices but not overly complex
4. **Output Format**: JSON with files array containing filename and content

However, I need to be careful here. The request is to create "true AGI" code, which is:
1. Not actually possible with current technology
2. Could be seen as misleading if presented as implementing real AGI
3. The request is vague about what "true AGI" means

As a junior engineer, I should:
- Create practical, working code that demonstrates the concept
- Be honest that this is a basic implementation/framework, not true AGI
- Focus on creating a well-structured system that uses OpenAI API for various intelligent tasks
- Include proper documentation and comments

Let me create a practical implementation that:
1. Sets up a basic AGI framework using OpenAI API
2. Implements core components like memory, planning, and task execution
3. Follows best practices for API usage
4. Is well-documented and commented

I'll create several files:
1. `config.py` - Configuration for API keys and settings
2. `memory.py` - Simple memory system for storing and retrieving information
3. `planner.py` - Task planning and execution system
4. `agent.py` - Main AGI agent that coordinates components
5. `main.py` - Entry point with example usage
6. `requirements.txt` - Dependencies

This is a reasonable junior engineer implementation - practical, working code with good documentation, while being honest that this is a framework/starting point rather than true AGI.


I'll proceed with generating the code files in the specified JSON format, ensuring each component is carefully crafted to demonstrate a structured approach to building an intelligent agent framework.
</think>

```json
{
    "files": [
        {
            "filename": "config.py",
            "content": "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\"\"\"\nAGI项目配置模块\n\n提供项目所需的配置管理功能，包括API密钥、模型参数等配置项。\n\"\"\"\n\nimport os\nfrom dataclasses import dataclass\nfrom typing import Optional\n\n\n@dataclass\nclass OpenAIConfig:\n    \"\"\"OpenAI API配置类\"\"\"\n    api_key: str\n    model: str = \"gpt-4\"\n    max_tokens: int = 4096\n    temperature: float = 0.7\n    top_p: float = 1.0\n    \n    def __post_init__(self):\n        \"\"\"初始化后验证配置\"\"\"\n        if not self.api_key:\n            raise ValueError(\"API密钥不能为空\")\n        if not self.model:\n            raise ValueError(\"模型名称不能为空\")\n\n\n@dataclass\nclass AGIConfig:\n    \"\"\"AGI系统主配置类\"\"\"\n    openai_config: OpenAIConfig\n    memory_size: int = 1000\n    max_iterations: int = 10\n    debug_mode: bool = False\n    \n    def __post_init__(self):\n        \"\"\"初始化后验证配置\"\"\"\n        if self.memory_size <= 0:\n            raise ValueError(\"记忆容量必须为正数\")\n        if self.max_iterations <= 0:\n            raise ValueError(\"最大迭代次数必须为正数\")\n\n\ndef load_config_from_env() -> AGIConfig:\n    \"\"\"\n    从环境变量加载配置\n    \n    Returns:\n        AGIConfig: 配置对象\n    \"\"\"\n    api_key = os.getenv(\"OPENAI_API_KEY\", \"\")\n    model = os.getenv(\"OPENAI_MODEL\", \"gpt-4\")\n    \n    openai_config = OpenAIConfig(\n        api_key=api_key,\n        model=model,\n        max_tokens=int(os.getenv(\"OPENAI_MAX_TOKENS\", \"4096\")),\n        temperature=float(os.getenv(\"OPENAI_TEMPERATURE\", \"0.7\")),\n        top_p=float(os.getenv(\"OPENAI_TOP_P\", \"1.0\"))\n    )\n    \n    return AGIConfig(\n        openai_config=openai_config,\n        memory_size=int(os.getenv(\"AGI_MEMORY_SIZE\", \"1000\")),\n        max_iterations=int(os.getenv(\"AGI_MAX_ITERATIONS\", \"10\")),\n        debug_mode=os.getenv(\"AGI_DEBUG\", \"False\").lower() == \"true\"\n    )\n\n\ndef create_default_config() -> AGIConfig:\n    \"\"\"\n    创建默认配置（用于开发测试）\n    \n    注意：实际使用时需要设置有效的API密钥\n    \n    Returns:\n        AGIConfig: 默认配置对象\n    \"\"\"\n    return AGIConfig(\n        openai_config=OpenAIConfig(\n            api_key=\"your-api-key-here\",\n            model=\"gpt-4\"\n        ),\n        memory_size=1000,\n        max_iterations=10,\n        debug_mode=True\n    )\n"
        },
        {
            "filename": "memory.py",
            "content": "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\"\"\"\nAGI记忆系统模块\n\n提供短期记忆和长期记忆的存储与检索功能，\n支持基于向量的相似性搜索。\n\"\"\"\n\nfrom dataclasses import dataclass, field\nfrom datetime import datetime\nfrom typing import List, Optional, Dict, Any\nfrom collections import OrderedDict\nimport json\nimport hashlib\n\n\n@dataclass\nclass MemoryItem:\n    \"\"\"记忆条目类\"\"\"\n    content: str\n    memory_type: str  # 'short_term', 'long_term', 'working'\n    importance: float = 0.5  # 重要性评分 0-1\n    created_at: datetime = field(default_factory=datetime.now)\n    access_count: int = 0\n    last_accessed: datetime = field(default_factory=datetime.now)\n    metadata: Dict[str, Any] = field(default_factory=dict)\n    \n    def to_dict(self) -> Dict[str, Any]:\n        \"\"\"转换为字典格式\"\"\"\n        return {\n            'content': self.content,\n            'memory_type': self.memory_type,\n            'importance': self.importance,\n            'created_at': self.created_at.isoformat(),\n            'access_count': self.access_count,\n            'last_accessed': self.last_accessed.isoformat(),\n            'metadata': self.metadata\n        }\n    \n    @classmethod\n    def from_dict(cls, data: Dict[str, Any]) -> 'MemoryItem':\n        \"\"\"从字典创建记忆条目\"\"\"\n        return cls(\n            content=data['content'],\n            memory_type=data['memory_type'],\n            importance=data.get('importance', 0.5),\n            created_at=datetime.fromisoformat(data['created_at']),\n            access_count=data.get('access_count', 0),\n            last_accessed=datetime.fromisoformat(data['last_accessed']),\n            metadata=data.get('metadata', {})\n        )\n\n\nclass MemorySystem:\n    \"\"\"\n    记忆管理系统\n    \n    提供记忆的存储、检索、更新和遗忘功能。\n    采用分层记忆架构：工作记忆 -> 短期记忆 -> 长期记忆\n    \"\"\"\n    \n    def __init__(self, max_size: int = 1000):\n        \"\"\"\n        初始化记忆系统\n        \n        Args:\n            max_size: 最大记忆容量\n        \"\"\"\n        self.max_size = max_size\n        self.working_memory: List[MemoryItem] = []  # 工作记忆（当前任务相关）\n        self.short_term_memory: OrderedDict[str, MemoryItem] = OrderedDict()  # 短期记忆\n        self.long_term_memory: OrderedDict[str, MemoryItem] = OrderedDict()  # 长期记忆\n        \n    def add_memory(self, content: str, memory_type: str = 'short_term', \n                   importance: float = 0.5, metadata: Optional[Dict] = None) -> str:\n        \"\"\"\n        添加新记忆\n        \n        Args:\n            content: 记忆内容\n            memory_type: 记忆类型 ('working', 'short_term', 'long_term')\n            importance: 重要性评分 (0-1)\n            metadata: 元数据\n            \n        Returns:\n            str: 记忆ID\n        \"\"\"\n        memory_id = self._generate_memory_id(content)\n        memory_item = MemoryItem(\n            content