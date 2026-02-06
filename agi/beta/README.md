# AGI 系统架构

这是一个基于 OpenAI API 的通用人工智能（AGI）系统架构原型。本项目采用模块化设计，包含记忆、推理和行动三大核心模块，旨在模拟人类认知流程。

## 架构特点

- **模块化设计**：每个功能组件（记忆、推理、行动）均可独立替换或扩展
- **可配置性**：通过 `AGIConfig` 控制系统行为（如是否启用记忆/推理）
- **上下文感知**：短期记忆维护对话历史，支持上下文理解
- **OpenAI 集成**：使用官方 OpenAI Python SDK

## 快速开始

1. 安装依赖：
   ```bash
   pip install openai
   ```

2. 设置环境变量：
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```

3. 运行示例：
   ```bash
   python agi_architecture.py
   ```

## 扩展方向

- 添加长期记忆持久化（如向量数据库）
- 实现工具调用（Function Calling）能力
- 集成多模态处理模块
- 增加自我反思与学习机制

> 注意：此架构为概念验证，真正的 AGI 需要更复杂的认知架构和持续学习能力。