# AGI项目架构

这是一个基于OpenAI API的通用人工智能(AGI)系统架构实现。

## 架构设计原则

1. **模块化设计**：将系统分解为记忆模块、推理引擎和核心协调器
2. **可扩展性**：通过抽象基类支持不同实现的替换
3. **上下文感知**：维护对话历史以提供连贯的交互体验
4. **配置驱动**：通过环境变量管理配置参数

## 核心组件

### MemoryModule (记忆模块)
- 负责存储和检索交互历史
- 当前实现：ShortTermMemory（短期记忆）
- 支持未来扩展长期记忆、向量数据库等

### ReasoningEngine (推理引擎)
- 处理输入并生成响应
- 当前实现：OpenAIReasoningEngine（基于OpenAI API）
- 支持未来集成其他LLM或混合推理策略

### AGICore (核心系统)
- 协调各组件工作流程
- 管理输入处理、上下文检索和响应生成

## 使用方法

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 配置环境变量：
```bash
cp .env.example .env
# 编辑.env文件，填入你的OpenAI API密钥
```

3. 运行系统：
```bash
python agi_architecture.py
```

## 扩展方向

- 添加长期记忆存储（如向量数据库）
- 实现多模态输入处理
- 集成工具使用能力（function calling）
- 添加自我反思和元认知能力
- 实现目标导向的行为规划