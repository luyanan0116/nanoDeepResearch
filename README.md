# nanoDeepResearch
OpenAI's [Deep Research](https://openai.com/index/introducing-deep-research/) is a really cool product. This project is inspired by ByteDance's [DeerFlow](https://github.com/bytedance/deer-flow) project, an open-source Deep Research project. DeerFlow is using [LangGraph](https://github.com/LangChain-AI/langgraph) to build the agentic workflow which abstracts away a lot of details, e.g. how the ReAct agent is working.

To make sure I understand how the DeerFlow's Deep Research agent works under the hood, I decided to build it from scratch without relying on any existing agentic framework, e.g. [LangGraph](https://www.langchain.com/langgraph).

Note that this project is currently pure backend without any frontend interface.

## Prepare the API keys

We need to prepare the API keys for the following services and store them as environment variables:
- OpenAI: `OPENAI_API_KEY`
- Claude: `ANTHROPIC_API_KEY`
- Tavily: `TAVILY_API_KEY`
- Jina: `JINA_API_KEY`



## Run the workflow

Go to the parent directory of this repo and run the following command:

```bash
python3 -m nanoDeepResearch.main \
--query "what is the area(land+water) ratio between the largest and smallest states in the US"
```

The example report can be found in `example_reports/area_ratio_largest_smallest_state_in_us.md`

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
