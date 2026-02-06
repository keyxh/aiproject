# agi

<think>The user is asking me to generate code for a project called "agi" (Artificial General Intelligence) that aims to implement a true AGI using OpenAI API. They want me to act as a senior engineer and generate practical, runnable code with best practices, comments, and documentation.

The output should be in JSON format with files containing code.

Let me think about what a realistic AGI implementation would look like. Since true AGI doesn't exist yet, I should create a framework that:
1. Provides a modular architecture for building AI agents
2. Uses OpenAI API as the core intelligence
3. Includes tools for reasoning, planning, and execution
4. Has proper error handling and logging
5. Follows best practices

I'll create a comprehensive project structure with:
1. Main agent core
2. Tool system for extending capabilities
3. Memory system for persistence
4. Planning module
5. Execution engine
6. Configuration management
7. API wrappers

Let me structure this as a Python project since it's the most common language for AI development.

Files to create:
1. `config.py` - Configuration management
2. `agent_core.py` - Main AGI agent implementation
3. `tools/base.py` - Base tool class
4. `tools/registry.py` - Tool registry system
5. `memory/memory.py` - Memory system
6. `planner/planner.py` - Planning module
7. `main.py` - Entry point
8. `requirements.txt` - Dependencies

Let me write comprehensive, production-ready code for each file.
</think>

```json
{
    "files": [
        {
            "filename": "config.py",
            "content": "\"\"\"\n项目配置模块\n负责管理AGI系统的所有配置参数\n\"\"\"\n\nimport os\nfrom dataclasses import dataclass\nfrom typing import Optional\nfrom pathlib import Path\n\n\n@dataclass\nclass OpenAIConfig:\n    \"\"\"OpenAI API配置\"\"\"\n    api_key: str = os.getenv(\"OPENAI_API_KEY\", \"\")\n    model: str = \"gpt-4-turbo-preview\"\n    max_tokens: int = 4096\n    temperature: float = 0.7\n    timeout: int = 120\n\n    def validate(self) -> bool:\n        \"\"\"验证配置是否有效\"\"\"\n        if not self.api_key:\n            raise ValueError(\"OpenAI API key未设置，请设置OPENAI_API_KEY环境变量\")\n        return True\n\n\n@dataclass\nclass AgentConfig:\n    \"\"\"Agent配置\"\"\"\n    name: str = \"AGI-Agent\"\n    description: str = \"一个通用人工智能代理\"\n    max_iterations: int = 100\n    reflection_depth: int = 3\n    enable_planning: bool = True\n    enable_memory: bool = True\n    enable_tools: bool = True\n\n\n@dataclass\nclass MemoryConfig:\n    \"\"\"记忆系统配置\"\"\"\n    storage_type: str = \"sqlite\"  # sqlite, redis, memory\n    db_path: str = \"./data/memory.db\"\n    max_memories: int = 10000\n    relevance_threshold: float = 0.7\n\n\n@dataclass\nclass LoggingConfig:\n    \"\"\"日志配置\"\"\"\n    level: str = \"INFO\"\n    format: str = \"%(asctime)s - %(name)s - %(levelname)s - %(message)s\"\n    file_path: Optional[str] = \"./logs/agi.log\"\n\n\n@dataclass\nclass AGIConfig:\n    \"\"\"AGI系统主配置\"\"\"\n    openai: OpenAIConfig\n    agent: AgentConfig\n    memory: MemoryConfig\n    logging: LoggingConfig\n\n    @classmethod\n    def load(cls, config_path: Optional[str] = None) -> \"AGIConfig\":\n        \"\"\"\n        加载配置\n        \n        Args:\n            config_path: 配置文件路径，支持.yaml格式\n            \n        Returns:\n            AGIConfig实例\n        \"\"\"\n        openai_config = OpenAIConfig()\n        openai_config.validate()\n        \n        return cls(\n            openai=openai_config,\n            agent=AgentConfig(),\n            memory=MemoryConfig(),\n            logging=LoggingConfig()\n        )\n\n\n# 默认配置实例\ndefault_config = AGIConfig.load()\n"
        },
        {
            "filename": "agent_core.py",
            "content": "\"\"\"\nAGI核心代理模块\n实现通用人工智能代理的核心逻辑\n\"\"\"\n\nimport json\nimport logging\nfrom typing import Dict, List, Optional, Any\nfrom dataclasses import dataclass, field\nfrom datetime import datetime\n\nfrom config import AGIConfig, default_config\nfrom memory.memory import MemorySystem, ShortTermMemory, LongTermMemory\nfrom planner.planner import Planner\nfrom tools.registry import ToolRegistry\n\n\nlogger = logging.getLogger(__name__)\n\n\n@dataclass\nclass Thought:\n    \"\"\"思维单元\"\"\"\n    role: str  # system, user, assistant\n    content: str\n    timestamp: datetime = field(default_factory=datetime.now)\n    metadata: Dict[str, Any] = field(default_factory=dict)\n\n\n@dataclass\nclass ActionResult:\n    \"\"\"行动结果\"\"\"\n    success: bool\n    result: Any\n    error: Optional[str] = None\n    execution_time: float = 0.0\n\n\nclass AGIAgent:\n    \"\"\"\n    AGI核心代理类\n    \n    实现功能:\n    1. 思维链推理 (Chain of Thought)\n    2. 工具调用 (Tool Use)\n    3. 记忆系统 (Memory System)\n    4. 自我反思 (Self-Reflection)\n    5. 规划与执行 (Planning & Execution)\n    \"\"\"\n\n    def __init__(self, config: AGIConfig = default_config):\n        \"\"\"\n        初始化AGI代理\n        \n        Args:\n            config: AGI配置对象\n        \"\"\"\n        self.config = config\n        self.conversation_history: List[Thought] = []\n        self.iteration_count = 0\n        \n        # 初始化各子系统\n        self._init_memory_system()\n        self._init_tool_system()\n        self._init_planning_system()\n        self._init_llm()\n        \n        logger.info(f\"AGI Agent '{self.config.agent.name}' 初始化完成\")\n\n    def _init_memory_system(self) -> None:\n        \"\"\"初始化记忆系统\"\"\"\n        if self.config.agent.enable_memory:\n            self.short_term_memory = ShortTermMemory(\n                max_memories=self.config.memory.max_memories\n            )\n            self.long_term_memory = LongTermMemory(\n                storage_type=self.config.memory.storage_type,\n                db_path=self.config.memory.db_path\n            )\n            logger.info(\"记忆系统初始化完成\")\n        else:\n            self.short_term_memory = None\n            self.long_term_memory = None\n\n    def _init_tool_system(self) -> None:\n        \"\"\"初始化工具系统\"\"\"\n        if self.config.agent.enable_tools:\n            self.tool_registry = ToolRegistry()\n            self._register_default_tools()\n            logger.info(f\"工具系统初始化完成，共{len(self.tool_registry)}个工具\")\n        else:\n            self.tool_registry = None\n\n    def _init_planning_system(self) -> None:\n        \"\"\"初始化规划系统\"\"\"\n        if self.config.agent.enable_planning:\n            self.planner = Planner(self)\n            logger.info(\"规划系统初始化完成\")\n        else:\n            self.planner = None\n\n    def _init_llm(self) -> None:\n        \"\"\"初始化大语言模型\"\"\"\n        try:\n            from openai import OpenAI\n            self.llm_client = OpenAI(\n                api_key=self.config.openai.api_key,\n                timeout=self.config.openai.timeout\n            )\n            self.model = self.config.openai.model\n            logger.info(f\"LLM初始化完成，使用模型: {self.model}\")\n        except Exception as e:\n            logger.error(f\"LLM初始化失败: {e}\")\n            raise\n\n    def _register_default_tools(self) -> None:\n        \"\"\"注册默认工具集\"\"\"\n        from tools.builtins import (\n            CalculatorTool,\n            SearchTool,\n            FileTool,\n            WebTool\n        )\n        \n        self.tool_registry.register(CalculatorTool())\n        self.tool_registry.register(SearchTool())\n        self.tool_registry.register(FileTool())\n        self.tool_registry.register(WebTool())\n\n    async def think(self, user_input: str) -> str:\n        \"\"\"\n        核心思维方法 - 处理用户输入并生成响应\n        \n        Args:\n            user_input: 用户输入\n            \n        Returns:\n            代理的响应\n        \"\"\"\n        self.iteration_count += 1\n        logger.info(f\"迭代 {self.iter