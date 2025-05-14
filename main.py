from .agent.react_agent import ReactAgent
from .tools.search import TavilySearchTool
from .llm.llm import OpenAIClient, AnthropicClient


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


agent = example_setup()
result = agent.run("What is the capital of the US?")
# Print the result
print("Final answer:", result["messages"][-1]["content"])
print("\nExecution trace:")
for i, step in enumerate(result["intermediate_steps"]):
    print(f"Step {i+1}:")
    print(f"  Thought: {step['thought']}")
    print(f"  Action: {step['action']}")
    print(f"  Action Input: {step['action_input']}")
    print(f"  Observation: {step['observation']}")
