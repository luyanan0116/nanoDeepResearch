# nanoDeepResearch
This project is inspired by ByteDance's [DeerFlow](https://github.com/bytedance/deer-flow) project, an open-source Deep Research project. DeerFlow is using Langgraph(https://github.com/LangChain-AI/langgraph) to build the agentic workflow which abstracts away a lot of details, e.g. how the ReAct agent is working.

To make sure I understand how the DeerFlow's Deep Research agent works under the hood, I decided to build it from scratch without relying on any existing agentic framework.

## ReAct Agent

The ReAct agent is a simple agent that uses a ReAct loop to reason and act. It is inspired by the ReAct paper: https://arxiv.org/abs/2210.03629

Given a task query, the ReAct agent will:
1. Reason about the task using the available tools
2. Act on the task using the available tools
3. Get the observation from the action results
4. Repeat the process until the task is completed

Note that all those steps are decided by the LLM without human intervention, really cool!

## State Machine(Graph)

`state_machine.py` is the class for the whole Deep Research workflow.
- Planner: the LLM of the planner agent will understand the user query and break it down into a list of task steps
- Research Team: it will take the list of task steps and assign each step to either a researcher agent or a coder agent
- Researcher: it is a ReAct agent and can use `web search` and `crawler` tools to solve the task
- Coder: it is a ReAct agent and can use `python` to solve the task
- Reporter: it will use the observations from the researcher and coder to generate the final report

## Lint

```bash
make lint
```

## Acknowledgement

Thanks to [DeerFlow](https://github.com/bytedance/deer-flow) for open-sourcing their project and providing a lot of inspiration.
