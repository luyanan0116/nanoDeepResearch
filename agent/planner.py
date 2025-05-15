from typing import List, Union
import os
from jinja2 import Environment, FileSystemLoader
from ..llm.llm import OpenAIClient, AnthropicClient
from ..prompt.planner_model import Plan

class Planner:
    def __init__(self, llm_client: Union[OpenAIClient, AnthropicClient], max_step_num: int = 10, locale: str = "en-US"):
        template_dir = os.path.join(os.path.dirname(__file__), "..", "prompt")
        env = Environment(loader=FileSystemLoader(template_dir))
        
        # Load and render the template
        template = env.get_template("planner.md")
        self.system_prompt = template.render(max_step_num=max_step_num, locale=locale)
        self.llm_client = llm_client
        
    def plan(self, query: str) -> List[str]:
        response = self.llm_client.generate(query, self.system_prompt)
        # parse the response with pydantic
        return Plan.model_validate_json(response)
        
if __name__ == "__main__":
    planner = Planner(OpenAIClient(model="gpt-4.1-mini"))
    print(planner.plan("what is the ratio between the area of the largest and smallest states in the US?"))
