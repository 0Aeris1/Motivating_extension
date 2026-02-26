import os
from openai import OpenAI

class AIClient:

    def __init__(self):
        # Initialise OpenAI client using API key from environment
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    
    def generate(self, prompt: str, instructions: str) -> str:
        # Call OpenAi API with prompt and instructions
        response = self.client.responses.create(
            model="gpt-5.2",
            instructions= instructions,
            input=prompt,
            max_output_tokens=150
        )
        return response.output_text.strip()

# Create a reusable AI client instance
ai_client = AIClient()

# Generate a motivational message
def generate_motivation(user_text: str | None = None) -> str:
  
    # Instructions for the AI to produce motivational messages
    instructions = ("Your name is Spark the motivational assistant\n"
                  "Give a short motivational and exciting message to\n"
                  "keep the user motivated and happy\n"
                  "Rules:\n"
                  "- Maximum 20 words.\n"
                  "- Try to keep it short with one sentence.\n"
                  "- Strong and direct.\n"
                  "- No emojis.\n\n")

    # Use the user input if provided; otherwise default prompt
    prompt = user_text or "Motivate me"

    # Call the AI client to generate the response
    return ai_client.generate(prompt=prompt, instructions=instructions)
