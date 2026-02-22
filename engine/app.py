import os

from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class AIClient:

    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def generate(self, prompt: str) -> str:
    # Calling OpenAI API
        response = self.client.responses.create(
            model="gpt-5.2",
            instructions="You are the happiest motivational assistant",
            input=prompt,
            max_output_tokens=150
        )
        return response.output_text.strip()

ai_client = AIClient()

class MotivationRequest(BaseModel):
    text: str

class MotivationResponse(BaseModel):
    response: str

def generate_motivation(user_text: str) -> str:
  
    prompt = (
            "You are my best motivator.\n"
            f"User: {user_text}\n"
            )

    return ai_client.generate(prompt)

app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_methods = ["*"],
        allow_headers = ["*"],
        allow_credentials = True
        )


@app.post("/motivate", response_model=MotivationResponse)
def motivate(req: MotivationRequest):
    reply = generate_motivation(req.text)

    return {"response": reply}


