# agi

 ```json
{
  "files": [
    {
      "filename": "requirements.txt",
      "content": "openai>=1.12.0\npydantic>=2.5.0\npydantic-settings>=2.1.0\npython-dotenv>=1.0.0\nnumpy>=1.26.0\naiohttp>=3.9.0\ntiktoken>=0.6.0"
    },
    {
      "filename": "config.py",
      "content": "\"\"\"\nAGI Project Configuration\n配置管理模块，使用Pydantic Settings管理环境变量和配置\n\"\"\"\nfrom pydantic_settings import BaseSettings\nfrom typing import Optional\n\n\nclass Settings(BaseSettings):\n    \"\"\"应用配置类\"\"\"\n    \n    # OpenAI API配置\n    openai_api_key: str\n    openai_base_url: Optional[str] = \"https://api.openai.com/v1\"\n    openai_model: str = \"gpt-4-turbo-preview\"  # 默认使用GPT-4 Turbo\n    \n    # 模型参数\n    temperature: float = 0.7\n    max_tokens: int = 4096\n    \n    # Agent配置\n    max_iterations: int = 10  # 最大思考-行动循环次数\n    context_window_size: int = 10  # 短期记忆窗口大小\n    \n    # 系统配置\n    debug: bool = False\n    log_level: str = \"INFO\"\n    \n    class Config:\n        env_file = \".env\"\n        env_file_encoding = \"utf-8\"\n\n\n# 全局配置实例\nsettings = Settings()\n"
    },
    {
      "filename": "models.py",
      "content": "\"\"\"\nAGI Project Data Models\n核心数据模型定义，使用Pydantic进行数据验证\n\"\"\"\nfrom pydantic import BaseModel, Field\nfrom typing import List, Dict, Any, Optional, Literal\nfrom datetime import datetime\nfrom enum import Enum\n\n\nclass ThoughtType(str, Enum):\n    \"\"\"思考类型枚举\"\"\"\n    PLANNING = \"planning\"      # 规划\n    REASONING = \"reasoning\"    # 推理\n    REFLECTION = \"reflection\"  # 反思\n    DECISION = \"decision\"      # 决策\n\n\nclass Thought(BaseModel):\n    \"\"\"思考记录模型\"\"\"\n    type: ThoughtType\n    content: str\n    timestamp: datetime = Field(default_factory=datetime.now)\n    step: int  # 思考步骤序号\n\n\nclass Action(BaseModel):\n    \"\"\"行动模型\"\"\"\n    tool_name: str\n    parameters: Dict[str, Any]\n    thought: str  # 执行此行动的理由\n    step: int\n\n\nclass Observation(BaseModel):\n    \"\"\"观察结果模型\"\"\"\n    action_step: int  # 对应的行动步骤\n    result: str\n    success: bool\n    timestamp: datetime = Field(default_factory=datetime.now)\n\n\nclass MemoryEntry(BaseModel):\n    \"\"\"记忆条目模型\"\"\"\n    id: str\n    content: str\n    importance: float = Field(ge=0.0, le=1.0)  # 重要性评分\n    timestamp: datetime = Field(default_factory=datetime.now)\n    metadata: Dict[str, Any] = Field(default_factory=dict)\n    embedding: Optional[List[float]] = None  # 向量嵌入\n\n\nclass Task(BaseModel):\n    \"\"\"任务模型\"\"\"\n    id: str\n    description: str\n    status: Literal[\"pending\", \"in_progress\", \"completed\", \"failed\"] = \"pending\"\n    priority: int = Field(ge=1, le=5, default=3)\n    subtasks: List[str] = Field(default_factory=list)\n    created_at: datetime = Field(default_factory=datetime.now)\n    completed_at: Optional[datetime] = None\n\n\nclass AgentState(BaseModel):\n    \"\"\"Agent状态模型\"\"\"\n    current_task: Optional[Task] = None\n    thought_history: List[Thought] = Field(default_factory=list)\n    action_history: List[Action] = Field(default_factory=list)\n    observation_history: List[Observation] = Field(default_factory=list)\n    iteration_count: int = 0\n    is_running: bool = False\n"
    },
    {
      "filename": "memory.py",
      "content": "\"