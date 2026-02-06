# agi

<think>The user is asking me to generate code for an AGI (Artificial General Intelligence) project using OpenAI API. As a senior engineer, I need to generate practical, runnable code that follows best practices.

Let me think about what an AGI implementation might look like. Since this is about creating a "true AGI" using OpenAI API, I should design a system that:

1. Has a core reasoning engine
2. Can learn and adapt
3. Has memory and context management
4. Can use tools and take actions
5. Has planning capabilities
6. Follows safety guidelines

I'll create a modular architecture with:
- A main AGI controller
- Memory system (short-term and long-term)
- Tool/Action system
- Planning system
- Safety/alignment module
- Configuration management

Let me structure the code files:

1. `agi_core.py` - Main AGI class
2. `memory.py` - Memory management system
3. `tools.py` - Tool/Action system
4. `planner.py` - Planning and reasoning system
5. `config.py` - Configuration
6. `main.py` - Entry point
7. `requirements.txt` - Dependencies

I'll write comprehensive code with proper comments and documentation. Since this is a complex system, I'll make it practical while acknowledging that true AGI is still an active research area.

Let me generate the JSON output with all the files.
</think>

```json
{
    "files": [
        {
            "filename": "requirements.txt",
            "content": "# AGI Project Dependencies\nopenai>=1.0.0\npython-dotenv>=1.0.0\nloguru>=0.7.0\npydantic>=2.0.0\ntiktoken>=0.4.0\nredis>=4.5.0\nsqlalchemy>=2.0.0\n\n# Development dependencies\npytest>=7.0.0\nblack>=23.0.0\nmypy>=1.0.0"
        },
        {
            "filename": "config.py",
            "content": "\"\"\"\nAGI项目配置模块\n负责管理所有配置项，支持环境变量和配置文件加载\n\n作者: AGI Team\n版本: 1.0.0\n\"\"\"\n\nimport os\nfrom pathlib import Path\nfrom typing import Optional\nfrom dotenv import load_dotenv\nfrom pydantic import BaseModel, Field\n\n\nclass OpenAIConfig(BaseModel):\n    \"\"\"OpenAI API配置\"\"\"\n    api_key: str = Field(default=\"\", description=\"OpenAI API密钥\")\n    base_url: str = Field(default=\"https://api.openai.com/v1\", description=\"API基础URL\")\n    model: str = Field(default=\"gpt-4-turbo\", description=\"使用的模型名称\")\n    max_tokens: int = Field(default=4096, description=\"最大输出token数\")\n    temperature: float = Field(default=0.7, description=\"采样温度\")\n    timeout: int = Field(default=60, description=\"请求超时时间(秒)\")\n\n\nclass MemoryConfig(BaseModel):\n    \"\"\"记忆系统配置\"\"\"\n    short_term_capacity: int = Field(default=100, description=\"短期记忆容量\")\n    long_term_db_path: str = Field(default=\"./data/long_term_memory.db\", description=\"长期记忆数据库路径\")\n    embedding_model: str = Field(default=\"text-embedding-3-small\", description=\"嵌入模型名称\")\n    similarity_threshold: float = Field(default=0.8, description=\"相似度阈值\")\n\n\nclass SafetyConfig(BaseModel):\n    \"\"\"安全配置\"\"\"\n    max_actions_per_turn: int = Field(default=10, description=\"每轮最大操作数\")\n    require_confirmation: bool = Field(default=True, description=\"是否需要确认危险操作\")\n    banned_keywords: list = Field(default_factory=lambda: [\"delete\", \"destroy\", \"harm\"], description=\"禁止的关键词\")\n\n\nclass AGIConfig(BaseModel):\n    \"\"\"AGI主配置\"\"\"\n    openai: OpenAIConfig = Field(default_factory=OpenAIConfig)\n    memory: MemoryConfig = Field(default_factory=MemoryConfig)\n    safety: SafetyConfig = Field(default_factory=SafetyConfig)\n    log_level: str = Field(default=\"INFO\", description=\"日志级别\")\n    system_prompt: str = Field(default=\"\", description=\"系统提示词\")\n    \n    @classmethod\n    def load_from_env(cls, config_path: Optional[str] = None) -> \"AGIConfig\":\n        \"\"\"\n        从环境变量加载配置\n        \n        Args:\n            config_path: 可选的配置文件路径\n            \n        Returns:\n            AGIConfig: 配置实例\n        \"\"\"\n        # 加载.env文件\n        load_dotenv(config_path)\n        \n        # 构建OpenAI配置\n        openai_config = OpenAIConfig(\n            api_key=os.getenv(\"OPENAI_API_KEY\", \"\"),\n            base_url=os.getenv(\"OPENAI_BASE_URL\", \"https://api.openai.com/v1\"),\n            model=os.getenv(\"OPENAI_MODEL\", \"gpt-4-turbo\"),\n            max_tokens=int(os.getenv(\"OPENAI_MAX_TOKENS\", \"4096\")),\n            temperature=float(os.getenv(\"OPENAI_TEMPERATURE\", \"0.7\")),\n            timeout=int(os.getenv(\"OPENAI_TIMEOUT\", \"60\")),\n        )\n        \n        # 构建记忆配置\n        memory_config = MemoryConfig(\n            short_term_capacity=int(os.getenv(\"MEMORY_SHORT_TERM_CAPACITY\", \"100\")),\n            long_term_db_path=os.getenv(\"MEMORY_DB_PATH\", \"./data/long_term_memory.db\"),\n            embedding_model=os.getenv(\"EMBEDDING_MODEL\", \"text-embedding-3-small\"),\n            similarity_threshold=float(os.getenv(\"SIMILARITY_THRESHOLD\", \"0.8\")),\n        )\n        \n        # 构建安全配置\n        safety_config = SafetyConfig(\n            max_actions_per_turn=int(os.getenv(\"MAX_ACTIONS_PER_TURN\", \"10\")),\n            require_confirmation=os.getenv(\"REQUIRE_CONFIRMATION\", \"true\").lower() == \"true\",\n            banned_keywords=os.getenv(\"BANNED_KEYWORDS\", \"delete,destroy,harm\").split(\",\"),\n        )\n        \n        return cls(\n            openai=openai_config,\n            memory=memory_config,\n            safety=safety_config,\n            log_level=os.getenv(\"LOG_LEVEL\", \"INFO\"),\n            system_prompt=os.getenv(\"SYSTEM_PROMPT\", \"\"),\n        )\n\n\ndef create_default_system_prompt() -> str:\n    \"\"\"\n    创建默认的系统提示词\n    \n    Returns:\n        str: 系统提示词\n    \"\"\"\n    return \"\"\"你是一个通用人工智能助手，具备以下能力：\n1. 理解自然语言输入\n2. 进行逻辑推理和问题解决\n3. 学习和记忆信息\n4. 使用工具完成复杂任务\n5. 规划和执行多步骤任务\n\n请始终保持 helpful、honest 和 harmless 的原则。\n\"\"\"\n"
        },
        {
            "filename": "memory.py",
            "content": "\"\"\"\nAGI记忆系统模块\n负责管理短期记忆和长期记忆，支持记忆的存储、检索和遗忘\n\n作者: AGI Team\n版本: 1.0.0\n\"\"\"\n\nimport json\nimport uuid\nimport time\nfrom typing import Optional, List, Dict, Any, Tuple\nfrom dataclasses import dataclass, field\nfrom datetime import datetime\nfrom pathlib import Path\nfrom loguru import logger\nfrom pydantic import BaseModel\n\n\n@dataclass\nclass MemoryItem:\n    \"\"\"记忆项数据类\"\"\"\n    id: str = field(default_factory=lambda: str(uuid.uuid4()))\n    content: str = \"\"\n    memory_type: str = \"episodic\"  # episodic, semantic, procedural\n    importance: float = 0.5  # 0-1 重要性评分\n    created_at: float = field(default_factory=time.time)\n    last_accessed: float = field(default_factory=time.time)\n    access_count: int = 0\n    metadata: Dict[str, Any] = field(default_factory=dict)\n    embedding: Optional[List[float]] = None\n\n\nclass ShortTermMemory:\n    \"\"\"\n    短期记忆管理器\n    采用FIFO策略管理有限的短期记忆容量\n    \"\"\"\n    \n    def __init__(self, capacity: int = 100):\n        \"\"\"\n        初始化短期记忆管理器\n        \n        Args:\n            capacity: 最大记忆容量\n        \"\"\"\n        self.capacity = capacity\n        self.memories: List[MemoryItem] = []\n        logger.info(f\"短期记忆系统初始化完成，容量: {capacity}\")\n    \n    def add(self, content: str, memory