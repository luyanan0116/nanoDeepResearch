# Example usage with a specific LLM client (OpenAI in this case)
import os


class OpenAIClient:
    """Example OpenAI client for the React agent."""

    def __init__(self, model: str = "gpt-4.1-mini"):
        """Initialize the OpenAI client.

        Args:
            api_key: OpenAI API key
            model: Model to use (default: gpt-4)
        """
        import openai

        openai_api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=openai_api_key)
        self.model = model

    def generate(self, prompt: str, system_prompt: str="") -> str:
        """Generate a response from the OpenAI API.

        Args:
            prompt: The prompt to send to the API

        Returns:
            Generated text response
        """
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            # prevent the model from generating the observation as we want to use the tool
            stop=["Observation:"],
        )
        return response.choices[0].message.content


class AnthropicClient:
    """Example Anthropic client for the React agent."""

    def __init__(self, model: str = "claude-3-sonnet-20240229"):
        """Initialize the Anthropic client.

        Args:
            api_key: Anthropic API key
            model: Model to use (default: claude-3-sonnet-20240229)
        """
        import anthropic

        anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = anthropic.Anthropic(api_key=anthropic_api_key)
        self.model = model

    def generate(self, prompt: str, system_prompt: str="") -> str:
        """Generate a response from the Anthropic API.

        Args:
            prompt: The prompt to send to the API

        Returns:
            Generated text response
        """
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            messages=messages,
            # prevent the model from generating the observation as we want to use the tool
            stop_sequences=["Observation:"],
        )
        return response.content[0].text
