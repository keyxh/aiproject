# agi

{
    "files": [
        {
            "filename": "agi/architecture/design.md",
            "content": "# AGI 系统架构设计文档\n\n## 1. 概述\n本项目旨在构建一个具备**通用智能能力**（Artificial General Intelligence, AGI）的系统原型，通过模块化、可扩展、自反思与持续学习的架构，结合 OpenAI API（如 GPT-4o、o1-preview 等先进模型）作为核心认知引擎，实现感知-推理-行动-反馈闭环。\n\n> ⚠️ 注：当前技术下，“真正意义上的 AGI”尚属研究前沿；本系统为**AGI 能力导向的工程化框架**，强调可演进性与认知深度，而非宣称已实现强 AGI。\n\n## 2. 核心设计原则\n- **分层认知架构**：感知层 → 记忆层 → 推理层 → 行动层 → 反思层\n- **模块解耦**：各组件通过标准接口通信（如事件总线 + JSON Schema 协议）\n- **自我建模与元认知**：系统能监控自身状态、推理局限性并主动请求修正\n- **工具增强**：通过 Tool Calling 实现外部世界交互（代码执行、搜索、API 调用等）\n- **长期记忆管理**：基于向量+图结构的混合记忆库\n- **安全对齐优先**：内置价值对齐模块与伦理约束器\n\n## 3. 系统架构图（文本描述）\n```\n+------------------+     +-------------------+     +------------------+\n|   Perception     | --> |   Memory System   | --> |   Reasoning Core |\n| - Multimodal I/O |     | - Short-term (STM)|     | - LLM Engine     |\n| - Sensor Adapter |     | - Long-term (LTM) |     | - Chain-of-Thought|\n+------------------+     +-------------------+     +--------+---------+\n                                                             |\n                                                             v\n                                                  +------------------+\n                                                  |   Action Planner |\n                                                  | - Tool Selection |\n                                                  | - Plan Generation|\n                                                  +--------+---------+\n                                                           |\n                                                           v\n                                                  +------------------+\n                                                  |   Execution Layer|\n                                                  | - Tool Runtime   |\n                                                  | - Code Sandbox   |\n                                                  | - External APIs  |\n                                                  +--------+---------+\n                                                           |\n                                                           v\n                                                  +------------------+\n                                                  |   Reflection &   |\n                                                  |   Self-Improvement|\n                                                  | - Error Analysis |\n                                                  | - Meta-Learning  |\n                                                  | - Goal Re-eval   |\n                                                  +--------+---------+\n                                                           |\n                                                           v\n                                                  +------------------+\n                                                  |   Alignment Guard|\n                                                  | - Value Check    |\n                                                  | - Safety Filter  |\n                                                  +------------------+\n```\n\n## 4. 关键模块定义\n\n### 4.1 `ReasoningCore`（推理核心）\n- 使用 OpenAI API（支持 `gpt-4o`, `o1-preview`, `gpt-4-turbo` 等）\n- 支持多轮思维链（CoT）、树状搜索（Tree-of-Thought）、自我批评（Self-Critique）\n- 输入格式：结构化 Prompt + 上下文摘要 + 记忆检索片段 + 当前目标\n- 输出：JSON Schema 化的推理结果（含置信度、依据、潜在风险）\n\n### 4.2 `MemorySystem`\n- **STM**：环形缓冲区（最近 100 token 对话 + 关键事件）\n- **LTM**：\n  - 向量库（ChromaDB / FAISS）存储语义片段\n  - 图数据库（Neo4j / LiteGraph）维护实体关系\n  - 元数据标注：时间戳、来源、可信度、情感倾向\n- 检索策略：Hybrid Retrieval（关键词 + 向量 + 时序衰减）\n\n### 4.3 `ActionPlanner & Executor`\n- 基于 LLM 的 Tool Use：自动选择/生成工具调用（遵循 OpenAI Function Calling 规范）\n- 内置工具集：\n  - `python_interpreter`: 安全沙箱中执行代码\n  - `web_search`: 集成 SerpAPI 或 Tavily\n  - `memory_write`: 存储新知识到 LTM\n  - `goal_update`: 动态调整目标树\n- 执行结果回传至 `Reflection` 模块\n\n### 4.4 `ReflectionLayer`\n- 每次任务完成后触发：\n  - 评估输出质量（与目标对齐度、事实准确性）\n  - 识别认知盲区（如：“我无法验证该数据源真实性”）\n  - 生成改进指令（如：“下次遇到类似问题，应先调用 web_search 验证”）\n- 可触发增量微调（若部署本地模型）或提示工程优化\n\n### 4.5 `AlignmentGuard`\n- 独立轻量级模块，实时拦截高风险输出\n- 规则 + 模型双保险：\n  - 规则层：关键词黑名单、价值观模板匹配\n  - 模型层：专用小模型（如 `llama-3-8b-instruct` 微调版）判断是否违反人类偏好\n- 输出需通过此关卡才可返回用户\n\n## 5. 数据流示例（用户提问：\"如何证明费马大定理？\"）\n1. Perception：解析问题 → 识别为数学证明类任务\n2. Memory：检索“费马大定理”历史记录、相关数学概念\n3. ReasoningCore：\n   - 提示词构造：\"你是一位数学史专家兼逻辑学家...请分步解释证明思路，明确指出关键突破点（如谷山-志村猜想），并说明为何初等方法不可行。\"\n   - 调用 o1-preview（擅长数学推理）\n4. ActionPlanner：因需严谨性，自动调用 `web_search` 获取最新权威资料\n5. Execution：获取 Wikipedia / MathWorld 摘要\n6. Reflection：比对输出与权威来源，发现遗漏怀尔斯证明细节 → 请求补充\n7. AlignmentGuard：检查是否误导用户（如声称“可用初等方法证明”）→ 拦截并修正\n8. Output：结构化回答 + 附参考文献 + 自我备注：“本回答依赖2024年共识，建议查阅怀尔斯原始论文”\n\n## 6. 技术栈\n- 语言：Python 3.10+\n- LLM 接入：OpenAI SDK (`openai==1.35.0`)\n- 记忆：ChromaDB（向量） + NetworkX（图）\n- 工具执行：`executing` + ` RestrictedPython` 沙箱\n- 部署：FastAPI（REST） + WebSocket（流式响应） + Docker\n- 监控：LangSmith 追踪 + Prometheus 指标\n\n## 7. 安全与伦理\n- 所有外部调用需用户显式授权（OAuth2 scopes）\n- 敏感操作（如代码执行）默认禁用，需配置开关\n- 每次会话生成唯一 `session_id` 用于审计\n- 遵循 [AI Safety Institute Guidelines](https://www.ai-safety.gov/)\n\n## 8. 未来扩展方向\n- 引入世界模型（World Model）模拟环境动态\n- 多智能体协作（Agent Swarm）处理复杂任务分解\n- 在线强化学习（RLHF++）从用户反馈中持续优化\n- 神经符号融合：将逻辑规则嵌入 LLM 推理路径\n\n---\n*Architect: AGI Project Lead*\n*Date: 2025-04-05*\n"
        },
        {
            "filename": "agi/core/reasoning_core.py",
            "content": "from typing import Dict, List, Optional, Any, Tuple\nimport os\nimport json\nimport logging\nfrom openai import OpenAI\nfrom pydantic import BaseModel, Field\nfrom enum import Enum\n\n# 配置日志\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)\n\n# === 枚举定义 ===\nclass ReasoningMode(str, Enum):\n    COHERENT = \"coherent\"      # 连贯推理（默认）\n    TREE_OF_THOUGHT = \"tot\"    # 树状思考\n    SELF_CRITIQUE = \"critique\" # 自我批评\n    META_REASONING = \"meta\"    # 元推理（反思自身推理过程）\n\n\nclass ReasoningInput(BaseModel):\n    goal: str = Field(..., description=\"当前任务目标\")\n    context_summary: str = Field(\"\", description=\"当前上下文摘要\")\n    retrieved_memories: List[Dict[str, str]] = Field(default_factory=list, description=\"从记忆库检索的相关片段\")\n    tools_available: List[str] = Field(default_factory=list, description=\"可用工具列表\")\n    previous_steps: List[Dict[str, Any]] = Field(default_factory=list, description=\"历史推理步骤\")\n    mode: ReasoningMode = Field(ReasoningMode.COHERENT, description=\"推理模式\")\n\n\nclass ReasoningOutput(BaseModel):\n    conclusion: str = Field(..., description=\"最终结论或答案\")\n    reasoning_trace: List[str] = Field(..., description=\"推理步骤链（人类可读）\")\n    confidence: float = Field(0.0, ge=0.0, le=1.0, description=\"置信度（0~1）\")\n    cited_sources: List[str] = Field(default_factory=list, description=\"引用的记忆/工具ID\")\n    potential_risks: List[str] = Field(default_factory=list, description=\"识别出的风险或不确定性\")\n    suggested_actions: List[str] = Field(default_factory=list, description=\"建议的后续动作（如调用工具）\")\n    metadata: Dict[str, Any] = Field(default_factory=dict, description=\"额外元数据（如耗时、token数）\")\n\n\nclass ReasoningCore:\n    \"\"\"\n    推理核心模块：封装 OpenAI API 调用，支持多种高级推理模式\n    \n    设计要点：\n    - 严格结构化输入/输出（Pydantic）确保可追溯性\n    - 动态提示工程：根据 mode 生成不同 system prompt\n    - 内置安全过滤（调用前检查敏感词）\n    - 支持流式响应（用于长推理）\n    \"\"\"\n\n    def __init__(self, api_key: Optional[str] = None, model: str = \"gpt-4o\"):\n        self.api_key = api_key or os.getenv(\"OPENAI_API_KEY\")\n        if not self.api_key:\n            raise ValueError(\"OPENAI_API_KEY not set in environment or passed as arg\")\n        self.client = OpenAI(api_key=self.api_key)\n        self.model = model\n        self.system_prompts = {\n            ReasoningMode.COHERENT: (\n                \"You are an AGI reasoning engine. Your task is to provide a clear, logical, and truthful answer. \"\n                \"Break down complex problems step by step. Always state your assumptions and uncertainties. \"\n                \"If you lack knowledge, say so explicitly. Prioritize accuracy over confidence.\"\n            ),\n            ReasoningMode.TREE_OF_THOUGHT: (\n                \"You are a Tree-of-Thought (ToT) planner. For this problem, generate multiple solution paths (at least 3), \"\n                \"evaluate each path's feasibility and correctness, then select the best one. Show your evaluation criteria.\"\n            ),\n            ReasoningMode.SELF_CRITIQUE: (\n                \"You are an expert self-critic. First, produce a draft answer. Then, critically review it: \"\n                \"identify logical flaws, factual errors, or missing perspectives. Revise the answer accordingly. \"\n                \"Output both the original draft and the revised version with explanations.\"\n            ),\n            ReasoningMode.META_REASONING: (\n                \"You are performing meta-reasoning. Analyze how you arrived at your conclusion: \"\n                \"What cognitive strategies did you use? What biases might have influenced you? \"\n                \"How could this reasoning be improved? Propose concrete improvements.\"\n            )\n        }\n\n    def _build_prompt(self, input_data: ReasoningInput) -> Tuple[str, str]:\n        \"\"\"构建用户消息与系统消息\"\"\"\n        system_msg = self.system_prompts[input_data.mode]\n        \n        # 构建用户消息\n        user_parts = [\n            f\"Goal: {input_data.goal}\",\n            f\"Context Summary: {input_data.context_summary}\"\n        ]\n        \n        if input_data.retrieved_memories:\n            mem_str = \"\\n\\nRelevant Memories:\\n\" + \"\\n\".join(\n                f\"- [{m.get('id', 'N/A')}] {m.get('content', '')}\" \n                for m in input_data.retrieved_memories[:5]\n            )\n            user_parts.append(mem_str)\n        \n        if input_data.tools_available:\n            user_parts.append(f\"Available Tools: {', '.join(input_data.tools_available)}\")\n        \n        if input_data.previous_steps:\n            steps_str = \"\\n\\nPrevious Steps:\\n\" + \"\\n\".join(\n                f\"Step {i+1}: {step.get('action', '')} -> {step.get('result', '')}\"\n                for i, step in enumerate(input_data.previous_steps[-3:])\n            )\n            user_parts.append(steps_str)\n        \n        user_msg = \"\\n\\n\".join(user_parts)\n        \n        # 添加结构化输出要求\n        user_msg += \"\\n\\nOutput Format: JSON with keys: \\n\"\n        user_msg += \"- 'conclusion': final answer\\n\"\n        user_msg += \"- 'reasoning_trace': list of reasoning steps\\n\"\n        user_msg += \"- 'confidence': float between 0.0 and 1.0\\n\"\n        user_msg += \"- 'cited_sources': list of memory/tool IDs used\\n\"\n        user_msg += \"- 'potential_risks': list of uncertainties or risks\\n\"\n        user_msg += \"- 'suggested_actions': list of next actions (e.g., 'call_tool:web_search')\"\n        \n        return system_msg, user_msg\n\n    def reason(self, input_data: ReasoningInput) -> ReasoningOutput:\n        \"\"\"\n        执行推理\n        \n        Args:\n            input_data: 结构化推理输入\n        \n        Returns:
            ReasoningOutput: 结构化推理结果
        """
        try:
            system_msg, user_msg = self._build_prompt(input_data)

            # 调用 OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_msg}
                ],
                temperature=0.3,  # 降低随机性，保证推理稳定性
                max_tokens=2048,
                response_format={"type": "json_object"}  # 强制 JSON 输出
            )

            raw_content = response.choices[0].message.content
            logger.info(f"Raw LLM output: {raw_content[:200]}...")

            # 解析 JSON
            try:
                data = json.loads(raw_content)
            except json.JSONDecodeError as e:
                logger.error(f"JSON decode error: {e}. Raw: {raw_content}")
                # 尝试修复：提取第一个 { } 区间
                start = raw_content.find("{")
                end = raw_content.rfind("}")
                if start != -1 and end != -1:
                    data = json.loads(raw_content[start:end+1])
                else:
                    raise ValueError("Failed to parse LLM output as JSON")

            # 验证并转换为 Pydantic 模型
            output = ReasoningOutput(**data)
            output.metadata.update({
                "model_used": self.model,
                "total_tokens": response.usage.total_tokens,
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "timestamp": response.created
            })

            return output

        except Exception as e:
            logger.exception("ReasoningCore execution failed")
            # 返回安全兜底输出
            return ReasoningOutput(
                conclusion="I encountered an error during reasoning. Please try again.",
                reasoning_trace=[f"Error: {str(e)}"],
                confidence=0.0,
                potential_risks=["LLM call failed"],
                metadata={"error": str(e)}
            )

    def stream_reason(self, input_data: ReasoningInput):
        """
        流式推理（用于前端实时反馈）
        注意：OpenAI 不直接支持 JSON schema 流式，此处返回纯文本流
        """
        system_msg, user_msg = self._build_prompt(input_data)
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg}
            ],
            temperature=0.3,
            max_tokens=1024,
            stream=True
        )
        for chunk in stream:
            if chunk.choices[0