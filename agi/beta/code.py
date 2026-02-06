# agi

 "files": [
    {
      "filename": "agi.py",
      "content": "'''\nAGI模块\n\n模块用于构建具有自主行为的AGI系统。\n\n函数:\n    run_agent_task(任务描述): 使用OpenAI模型执行任务。\n'''\n\n\n# AGI模块\n\nfrom openai import completion\n\ndef run_agent_task(task_description):\n    \"\"\"\n    使用OpenAI模型执行给定任务。\n    \n    参数:\n        task_description (str): 任务描述。\n    \n    返回:\n        str: 模型生成的输出。\n    \"\"\"\n    \n    # 任务描述设置\n    prompt = f\"执行任务：{task_description}\\n生成输出：\"\n    \n    # 模型调用设置\n    response = completion.create(\n        engine=\"davinci\",\n        prompt=prompt,\n        max_tokens=150\n    )\n    \n    return response.choices[0].text.strip()"
]