from .agent.react_agent import ReactAgent
from .tools.search import TavilySearchTool
from .llm.llm import OpenAIClient, AnthropicClient
from .agent.planner import Planner


# Example usage
def example_setup():
    # Create tool instances
    search_tool = TavilySearchTool()
    openai_model = "gpt-4.1-mini"
    # https://docs.anthropic.com/en/docs/intro-to-claude
    anthropic_model = "claude-3-5-haiku-20241022"
    openai_client = OpenAIClient(model=openai_model)
    anthropic_client = AnthropicClient(model=anthropic_model)

    # Create the React agent
    agent = ReactAgent(
        llm_client=anthropic_client,
        name="research agent",
        prompt="You are a research agent that solves tasks step by step.",
        tools=[search_tool],
    )

    return agent


# react_agent = example_setup()
# result = react_agent.run("What is the capital of the US?")
# # Print the result
# print("Final answer:", result["messages"][-1]["content"])
# print("\nExecution trace:")
# for i, step in enumerate(result["intermediate_steps"]):
#     print(f"Step {i+1}:")
#     print(f"  Thought: {step['thought']}")
#     print(f"  Action: {step['action']}")
#     print(f"  Action Input: {step['action_input']}")
#     print(f"  Observation: {step['observation']}")

planner = Planner(OpenAIClient(model="gpt-4.1-mini"))
plan = planner.plan(
    "what is the ratio between the area of the largest and smallest states in the US?"
)
print(f"has enough context: {plan.has_enough_context}")
print(f"thought: {plan.thought}")
print(f"title: {plan.title}")
for i, step in enumerate(plan.steps):
    print(f"step {i+1}:")
    print(f"title: {step.title}")
    print(f"description: {step.description}")
    print(f"step_type: {step.step_type}")
    print(f"execution_res: {step.execution_res}")
    print(f"need_web_search: {step.need_web_search}")
