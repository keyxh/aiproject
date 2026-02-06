# agi

<think>用户要求我作为高级工程师为项目"agi"生成代码，该项目旨在实现一个真正意义上的AGI（通用人工智能），使用OpenAI API。

我需要生成一个完整的、可运行的代码结构，包含必要的组件。考虑到AGI的复杂性，我需要设计一个模块化的架构，包括：

1. 核心AGI引擎
2. 任务规划和执行系统
3. 记忆系统
4. 工具调用系统
5. 对话和交互接口
6. 配置管理

让我设计一个实用的AGI系统架构：

- main.py: 主入口
- config.py: 配置管理
- core/agi_engine.py: 核心AGI引擎
- core/memory.py: 记忆系统
- core/planner.py: 任务规划器
- tools/base.py: 工具基类
- tools/search.py: 搜索工具
- tools/calculator.py: 计算工具
- api/openai_client.py: OpenAI API客户端
- requirements.txt: 依赖列表
- README.md: 文档

这是一个相当复杂的系统，我需要确保代码质量高、有适当的注释，并且可以运行。

让我开始生成代码：

首先，我需要确定JSON格式的输出结构。
</think>

```json
{
    "files": [
        {
            "filename": "requirements.txt",
            "content": "openai>=1.0.0\npydantic>=2.0.0\npython-dotenv>=1.0.0\nloguru>=0.7.0\ncoloredlogs>=15.0.0\ntiktoken>=0.5.0\nasyncio>=3.4.3\n"
        },
        {
            "filename": ".env.example",
            "content": "# OpenAI API Configuration\nOPENAI_API_KEY=your_api_key_here\nOPENAI_MODEL=gpt-4-turbo\nOPENAI_BASE_URL=https://api.openai.com/v1\n\n# AGI Configuration\nMAX_TOKENS=4096\nTEMPERATURE=0.7\nMAX_MEMORY_TOKENS=8000\nLOG_LEVEL=INFO\n"
        },
        {
            "filename": "config.py",
            "content": "\"\"\"\n配置管理模块\n负责加载和管理AGI系统的所有配置\n\"\"\"\n\nimport os\nfrom pathlib import Path\nfrom typing import Optional\nfrom dataclasses import dataclass, field\nfrom dotenv import load_dotenv\n\n\n@dataclass\nclass OpenAIConfig:\n    \"\"\"OpenAI API配置\"\"\"\n    api_key: str = \"\"\n    model: str = \"gpt-4-turbo\"\n    base_url: str = \"https://api.openai.com/v1\"\n    max_tokens: int = 4096\n    temperature: float = 0.7\n\n\n@dataclass\nclass MemoryConfig:\n    \"\"\"记忆系统配置\"\"\"\n    max_tokens: int = 8000\n    summary_interval: int = 5\n    importance_threshold: float = 0.7\n\n\n@dataclass\nclass AGIConfig:\n    \"\"\"AGI主配置\"\"\"\n    openai: OpenAIConfig = field(default_factory=OpenAIConfig)\n    memory: MemoryConfig = field(default_factory=MemoryConfig)\n    log_level: str = \"INFO\"\n    debug_mode: bool = False\n\n\nclass ConfigManager:\n    \"\"\"配置管理器\"\"\"\n    \n    def __init__(self, config_path: Optional[str] = None):\n        \"\"\"\n        初始化配置管理器\n        \n        Args:\n            config_path: 配置文件路径，如果为None则尝试加载.env文件\n        \"\"\"\n        self.config = AGIConfig()\n        \n        if config_path:\n            self._load_config_file(config_path)\n        else:\n            self._load_env_config()\n    \n    def _load_env_config(self):\n        \"\"\"从环境变量加载配置\"\"\"\n        load_dotenv()\n        \n        # OpenAI配置\n        self.config.openai.api_key = os.getenv(\"OPENAI_API_KEY\", \"\")\n        self.config.openai.model = os.getenv(\"OPENAI_MODEL\", \"gpt-4-turbo\")\n        self.config.openai.base_url = os.getenv(\"OPENAI_BASE_URL\", \"https://api.openai.com/v1\")\n        self.config.openai.max_tokens = int(os.getenv(\"MAX_TOKENS\", \"4096\"))\n        self.config.openai.temperature = float(os.getenv(\"TEMPERATURE\", \"0.7\"))\n        \n        # 记忆配置\n        self.config.memory.max_tokens = int(os.getenv(\"MAX_MEMORY_TOKENS\", \"8000\"))\n        \n        # 通用配置\n        self.config.log_level = os.getenv(\"LOG_LEVEL\", \"INFO\")\n        self.config.debug_mode = os.getenv(\"DEBUG_MODE\", \"false\").lower() == \"true\"\n    \n    def _load_config_file(self, config_path: str):\n        \"\"\"\n        从配置文件加载配置\n        \n        Args:\n            config_path: 配置文件路径（支持.yaml, .json, .env格式）\n        \"\"\"\n        path = Path(config_path)\n        \n        if path.suffix == \".env\":\n            self._load_env_config()\n        elif path.suffix == \".yaml\":\n            self._load_yaml_config(path)\n        elif path.suffix == \".json\":\n            self._load_json_config(path)\n    \n    def _load_yaml_config(self, path: Path):\n        \"\"\"加载YAML配置文件\"\"\"\n        import yaml\n        \n        with open(path, 'r', encoding='utf-8') as f:\n            data = yaml.safe_load(f)\n            \n        if data:\n            self._apply_config_dict(data)\n    \n    def _load_json_config(self, path: Path):\n        \"\"\"加载JSON配置文件\"\"\"\n        import json\n        \n        with open(path, 'r', encoding='utf-8') as f:\n            data = json.load(f)\n            \n        if data:\n            self._apply_config_dict(data)\n    \n    def _apply_config_dict(self, data: dict):\n        \"\"\"应用配置字典到配置对象\"\"\"\n        if \"openai\" in data:\n            oai = data[\"openai\"]\n            self.config.openai.api_key = oai.get(\"api_key\", self.config.openai.api_key)\n            self.config.openai.model = oai.get(\"model\", self.config.openai.model)\n        \n        if \"memory\" in data:\n            mem = data[\"memory\"]\n            self.config.memory.max_tokens = mem.get(\"max_tokens\", self.config.memory.max_tokens)\n    \n    def get_openai_config(self) -> OpenAIConfig:\n        \"\"\"获取OpenAI配置\"\"\"\n        return self.config.openai\n    \n    def get_memory_config(self) -> MemoryConfig:\n        \"\"\"获取记忆配置\"\"\"\n        return self.config.memory\n    \n    def get(self, key: str, default=None):\n        \"\"\"获取配置值\"\"\"\n        keys = key.split(\".\")\n        value = self.config\n        \n        for k in keys:\n            if hasattr(value, k):\n                value = getattr(value, k)\n            else:\n                return default\n        \n        return value\n    \n    def validate(self) -> bool:\n        \"\"\"验证配置有效性\"\"\"\n        if not self.config.openai.api_key:\n            return False\n        return True\n"
        },
        {
            "filename": "api/openai_client.py",
            "content": "\"\"\"\nOpenAI API客户端\n封装与OpenAI API的所有交互\n\"\"\"\n\nimport asyncio\nfrom typing import Optional, List, Dict, Any, Union\nfrom loguru import logger\nfrom openai import AsyncOpenAI\nfrom pydantic import BaseModel\n\nfrom config import OpenAIConfig\n\n\nclass Message(BaseModel):\n    \"\"\"消息模型\"\"\"\n    role: str  # \"system\", \"user\", \"assistant\", \"tool\"\n    content: str\n    name: Optional[str] = None\n    tool_calls: Optional[List[Dict]] = None\n    tool_call_id: Optional[str] = None\n\n\nclass ToolCall(BaseModel):\n    \"\"\"工具调用模型\"\"\"\n    id: str\n    type: str = \"function\"\n    function: Dict[str, str]\n\n\nclass OpenAIClient:\n    \"\"\"\n    OpenAI API客户端封装\n    \n    提供异步API调用能力，支持流式响应和工具调用\n    \"\"\"\n    \n    def __init__(self, config: OpenAIConfig):\n        \"\"\"\n        初始化OpenAI客户端\n        \n        Args:\n            config: OpenAI配置对象\n        \"\"\"\n        self.config = config\n        self.client = AsyncOpenAI(\n            api_key=config.api_key,\n            base_url=config.base_url,\n        )\n        logger.info(f