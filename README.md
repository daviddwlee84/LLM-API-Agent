# LLM-API-Agent

Creating tools for LLM so it can call API by itself and finish complex tasks

## Getting Started

Python 3.10+

```bash
pip install -r requirements.txt

# Fill your credential
cp example.env .env

# Adhoc
python ./utils/api.py
```

## Resources

### LangChain

Tools and Agent (general)

- [Agents | 🦜️🔗 Langchain](https://python.langchain.com/docs/modules/agents/)
  - [Tools | 🦜️🔗 Langchain](https://python.langchain.com/docs/modules/agents/tools/)
- [Choosing between multiple tools | 🦜️🔗 Langchain](https://python.langchain.com/docs/use_cases/tool_use/multiple_tools)
- [Agents | 🦜️🔗 Langchain](https://python.langchain.com/docs/use_cases/tool_use/agents)

API Agent and Planner

- [OpenAPI | 🦜️🔗 Langchain](https://python.langchain.com/docs/integrations/toolkits/openapi)

### Papers

Agents/Tools (general)

- [[2210.03629] ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)

API Agent (specific)

- [[2306.06624] RestGPT: Connecting Large Language Models with Real-World RESTful APIs](https://arxiv.org/abs/2306.06624)

### API Documents

- [APIs-guru/openapi-directory: 🌐 Wikipedia for Web APIs. Directory of REST API definitions in OpenAPI 2.0/3.x format](https://github.com/APIs-guru/openapi-directory)
- [APIs.guru](https://apis.guru/)
