# LLM API Agent

Creating tools for LLM so it can call API by itself and finish complex tasks.

Good example of how to play with Agents, Tools, etc.

## Getting Started

Python 3.10+

```bash
pip install -r requirements.txt

# Fill your credential
cp example.env .env

# Adhoc
python ./utils/api.py
```

## Todos

Infrastructure

- [X] OpenAPI document to API Agent
- [ ] General API document (e.g. using web crawler)
- [ ] Self-building API call function as tool

Learning

- [ ] Understand LangGraph

Bug

- [ ] Fix agent executor intermediate output exceed max token length limit issue

Tasks

- [ ] Spotify Agent
  - [X] Basic Spotify API call based on OpenAPI document
    - [X] Change it to notebook
    - [ ] Fix bug
  - [ ] JSON agent
- [ ] Financial Agent
  - [X] Simple Polygon
    - [ ] Fix bug
  - [ ] LangGraph + Polygon

Other

- [ ] Build UI to play with each of them (if there is stable playable example)

## Resources

### LangChain

Tools and Agent (general)

- [Agents | 🦜️🔗 Langchain](https://python.langchain.com/docs/modules/agents/)
  - [Tools | 🦜️🔗 Langchain](https://python.langchain.com/docs/modules/agents/tools/)
- [Choosing between multiple tools | 🦜️🔗 Langchain](https://python.langchain.com/docs/use_cases/tool_use/multiple_tools)
- [Agents | 🦜️🔗 Langchain](https://python.langchain.com/docs/use_cases/tool_use/agents)

API Agent and Planner

- [OpenAPI | 🦜️🔗 Langchain](https://python.langchain.com/docs/integrations/toolkits/openapi)
  - [langchain/libs/community/langchain_community/agent_toolkits/openapi at master · langchain-ai/langchain](https://github.com/langchain-ai/langchain/tree/master/libs/community/langchain_community/agent_toolkits/openapi)
  - [langchain/libs/community/tests/unit_tests/tools/openapi at master · langchain-ai/langchain](https://github.com/langchain-ai/langchain/tree/master/libs/community/tests/unit_tests/tools/openapi)
  - [langchain/docs/docs/integrations/toolkits/openapi.ipynb at master · langchain-ai/langchain](https://github.com/langchain-ai/langchain/blob/master/docs/docs/integrations/toolkits/openapi.ipynb)

Template

- [LangSmith](https://smith.langchain.com/hub)
  - [LangChain Hub | 🦜️🛠️ LangSmith](https://docs.smith.langchain.com/cookbook/hub-examples)
  - [hwchase17/langchain-hub](https://github.com/hwchase17/langchain-hub)
- [openai-functions-agent | 🦜️🔗 Langchain](https://python.langchain.com/docs/templates/openai-functions-agent)
  - [langchain/templates/openai-functions-agent at master · langchain-ai/langchain](https://github.com/langchain-ai/langchain/tree/master/templates/openai-functions-agent)

LangGraph

- [🦜🕸️LangGraph | 🦜️🔗 Langchain](https://python.langchain.com/docs/langgraph)
- [LangGraph: Multi-Agent Workflows](https://blog.langchain.dev/langgraph-multi-agent-workflows/)
  - [LangGraph: Multi-Agent Workflows - YouTube](https://www.youtube.com/watch?v=hvAPnpSfSGo)
- [Future of Coding — Multi-Agent LLM Framework using LangGraph | by Anurag Mishra | Mar, 2024 | Medium](https://medium.com/@anuragmishra_27746/future-of-coding-multi-agent-llm-framework-using-langgraph-092da9493663)
- [LangGraph](https://blog.langchain.dev/langgraph/)

### Papers

Agents/Tools (general)

- [[2210.03629] ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [[2205.00445] MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning](https://arxiv.org/abs/2205.00445)
  - [MRKL - Chainlit](https://docs.chainlit.io/examples/mrkl)
  - [whitead/robust-mrkl: A langchain agent that retries](https://github.com/whitead/robust-mrkl)

API Agent (specific)

- [[2306.06624] RestGPT: Connecting Large Language Models with Real-World RESTful APIs](https://arxiv.org/abs/2306.06624)

### API Documents

- [APIs-guru/openapi-directory: 🌐 Wikipedia for Web APIs. Directory of REST API definitions in OpenAPI 2.0/3.x format](https://github.com/APIs-guru/openapi-directory)
- [APIs.guru](https://apis.guru/)

### Others

- [自定义远程工具(Remote Tool) - ERNIE Bot Agent](https://ernie-bot-agent.readthedocs.io/zh-cn/stable/cookbooks/agent/remote_tool/)
