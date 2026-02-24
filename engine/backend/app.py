import os

from fastapi import FastAPI, HTTPException, Request, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from engine.backend.ai import generate_motivation
from engine.backend.schemas import MotivationRequest, MotivationResponse


limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
                status_code=429,
                content={"detail": "Slow down. Discipline builds greatness."}
            )

INTERNAL_API_KEY = os.getenv("INTERNAL_API_KEY")

def verify_api_key(x_internal_key: str = Header(None)):
    if x_internal_key != INTERNAL_API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")

app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_methods = ["*"],
        allow_headers = ["*"],
allow_credentials = True
        )


@app.post("/motivate", response_model=MotivationResponse)
@limiter.limit("5/day")
async def motivate(request: Request, req: MotivationRequest, _: None = Depends(verify_api_key)):
    try:
        reply = generate_motivation(req.text)
        return {"response": reply}
    except HTTPException:
        raise
    except Exception as e:
        print("ERROR:", e)   # or logging
        raise HTTPException(
            status_code=500,
            detail="AI malfunctioned. Or humanity did."
        )
