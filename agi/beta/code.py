# agi

<think>The user is asking me to generate code for a project called "agi" (Artificial General Intelligence) as a junior engineer. They want me to create actual, runnable code that follows best practices with necessary comments and documentation.

The response should be in JSON format with files containing filenames and content.

Let me think about what a junior engineer would create for an AGI project using OpenAI API:

1. A basic structure for an AGI system
2. Simple integration with OpenAI API
3. Basic error handling
4. Simple configuration management
5. Basic documentation

As a junior engineer, I should focus on:
- Clean, readable code
- Basic implementation
- Simple error handling
- Good documentation
- Following basic best practices

Let me create a simple but functional AGI framework using OpenAI API:

1. `config.py` - Configuration management
2. `agi_core.py` - Core AGI functionality
3. `main.py` - Main entry point
4. `requirements.txt` - Dependencies
5. `README.md` - Documentation

I'll create a modular structure that demonstrates understanding of basic software engineering principles while being practical and runnable.
</think>

```json
{
    "files": [
        {
            "filename": "config.py",
            "content": "#!/usr/bin/env python3\n\"\"\"\n配置文件 - 管理AGI系统的配置参数\n\n功能:\n- 集中管理所有配置参数\n- 支持环境变量覆盖\n- 提供类型检查和默认值\n\"\"\"\n\nimport os\nfrom typing import Optional\nfrom dataclasses import dataclass\n\n\n@dataclass\nclass OpenAIConfig:\n    \"\"\"OpenAI API配置类\"\"\"\n    api_key: str = os.getenv(\"OPENAI_API_KEY\", \"\")\n    model: str = os.getenv(\"OPENAI_MODEL\", \"gpt-4\")\n    max_tokens: int = int(os.getenv(\"OPENAI_MAX_TOKENS\", \"4096\"))\n    temperature: float = float(os.getenv(\"OPENAI_TEMPERATURE\", \"0.7\"))\n    timeout: int = int(os.getenv(\"OPENAI_TIMEOUT\", \"30\"))\n\n\n@dataclass\nclass AGIConfig:\n    \"\"\"AGI系统主配置类\"\"\"\n    openai: OpenAIConfig = None\n    debug_mode: bool = bool(os.getenv(\"DEBUG_MODE\", \"False\"))\n    log_level: str = os.getenv(\"LOG_LEVEL\", \"INFO\")\n    memory_size: int = int(os.getenv(\"MEMORY_SIZE\", \"1000\"))\n    \n    def __post_init__(self):\n        \"\"\"初始化后处理，设置默认值\"\"\"\n        if self.openai is None:\n            self.openai = OpenAIConfig()\n\n\ndef load_config(config_path: Optional[str] = None) -> AGIConfig:\n    \"\"\"\n    加载配置文件\n    \n    Args:\n        config_path: 配置文件路径，默认为None\n        \n    Returns:\n        AGIConfig: 配置对象\n    \"\"\"\n    config = AGIConfig()\n    \n    # 这里可以扩展为从YAML/JSON文件加载配置\n    # 目前使用环境变量和默认值\n    \n    return config\n"
        },
        {
            "filename": "agi_core.py",
            "content": "#!/usr/bin/env python3\n\"\"\"\nAGI核心模块 - 实现通用人工智能的基本功能\n\n功能:\n- 任务理解和分解\n- 上下文记忆管理\n- 工具调用和执行\n- 自我学习和改进\n\"\"\"\n\nfrom typing import List, Dict, Any, Optional\nfrom dataclasses import dataclass, field\nfrom datetime import datetime\nimport json\nimport logging\n\n\n# 配置日志\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)\n\n\n@dataclass\nclass Memory:\n    \"\"\"记忆单元类\"\"\"\n    content: str\n    timestamp: datetime = field(default_factory=datetime.now)\n    importance: float = 0.5\n    category: str = \"general\"\n\n\n@dataclass \nclass Task:\n    \"\"\"任务类\"\"\"\n    description: str\n    status: str = \"pending\"  # pending, in_progress, completed, failed\n    subtasks: List['Task'] = field(default_factory=list)\n    result: Optional[str] = None\n    created_at: datetime = field(default_factory=datetime.now)\n\n\nclass ContextMemory:\n    \"\"\"\n    上下文记忆管理器\n    \n    功能:\n    - 短期记忆：当前对话上下文\n    - 长期记忆：重要信息和经验\n    \"\"\"\n    \n    def __init__(self, max_size: int = 1000):\n        self.short_term_memory: List[Memory] = []\n        self.long_term_memory: List[Memory] = []\n        self.max_size = max_size\n    \n    def add_to_short_term(self, content: str, importance: float = 0.5):\n        \"\"\"添加短期记忆\"\"\"\n        memory = Memory(content=content, importance=importance, category=\"short_term\")\n        self.short_term_memory.append(memory)\n        \n        # 保持记忆在最大大小内\n        if len(self.short_term_memory) > self.max_size:\n            # 移除最不重要的记忆\n            self.short_term_memory.sort(key=lambda x: x.importance)\n            self.short_term_memory = self.short_term_memory[-self.max_size:]\n    \n    def add_to_long_term(self, content: str, importance: float = 0.8):\n        \"\"\"添加长期记忆\"\"\"\n        memory = Memory(content=content, importance=importance, category=\"long_term\")\n        self.long_term_memory.append(memory)\n        logger.info(f\"保存长期记忆: {content[:50]}...\")\n    \n    def get_relevant_memories(self, query: str, limit: int = 5) -> List[str]:\n        \"\"\"获取与查询相关的记忆\"\"\"\n        # 简单实现：基于关键词匹配\n        # 实际应用中可以使用向量数据库进行语义搜索\n        relevant = []\n        \n        all_memories = self.short_term_memory + self.long_term_memory\n        for memory in all_memories:\n            if query.lower() in memory.content.lower():\n                relevant.append(memory.content)\n                \n        return relevant[:limit]\n    \n    def clear_short_term(self):\n        \"\"\"清空短期记忆\"\"\"\n        self.short_term_memory = []\n\n\nclass TaskDecomposer:\n    \"\"\"\n    任务分解器\n    \n    功能:\n    - 将复杂任务分解为子任务\n    - 规划执行顺序\n    - 跟踪任务进度\n    \"\"\"\n    \n    def __init__(self):\n        self.task_queue: List[Task] = []\n        self.completed_tasks: List[Task] = []\n        self.failed_tasks: List[Task] = []\n    \n    def decompose_task(self, task_description: str) -> List[Task]:\n        \"\"\"\n        分解任务为子任务\n        \n        Args:\n            task_description: 任务描述\n            \n        Returns:\n            List[Task]: 子任务列表\n        \"\"\"\n        # 简单实现：基于规则的任务分解\n        # 实际应用中可以使用LLM进行智能分解\n        subtasks = []\n        \n        # 模拟任务分解逻辑\n        if \"和\" in task_description or \"以及\" in task_description:\n            # 处理包含多个子任务的复合任务\n            parts = task_description.replace(\"和\", \",\").replace(\"以及\", \",\").split(\",\")\n            for part in parts:\n                part = part.strip()\n                if part:\n                    subtasks.append(Task(description=part))\n        else:\n            # 单任务\n            subtasks.append(Task(description=task_description))\n        \n        self.task_queue.extend(subtasks)\n        return subtasks\n    \n    def get_next_task(self) -> Optional[Task]:\n        \"\"\"获取下一个待执行任务\"\"\"\n        if self.task_queue:\n            return self.task_queue[0]\n        return None\n    \n    def complete_task(self, task: Task, result: str):\n        \"\"\"标记任务完成\"\"\"\n        task.status = \"completed\"\n        task.result = result\n        \n        if task in self.task_queue:\n            self.task_queue.remove(task)\n        self.completed_tasks.append(task)\n    \n    def fail_task(self, task: Task, error: str):\n        \"\"\"标记任务失败\"\"\"\n        task.status = \"failed\"\n        task.result = error\n        \n        if task in self.task_queue:\n            self.task_queue.remove(task)\n        self.failed_tasks.append(task)\n\n\nclass AGICore:\n    \"\"\"\n    AGI核心引擎\n    \n    功能:\n    - 协调各组件工作\n    - 处理用户输入