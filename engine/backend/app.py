from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from ai import generate_motivation
from schemas import MotivationRequest, MotivationResponse


limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
                status_code=429,
                content={"detail": "Slow down. Discipline builds greatness."}
            )

app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_methods = ["*"],
        allow_headers = ["*"],
        allow_credentials = True
        )


@app.post("/motivate", response_model=MotivationResponse)
@limiter.limit("5/day")
def motivate(req: MotivationRequest, request: Request):
    try:
        reply = generate_motivation(req.text)

        return {"response": reply}
    except Exception:
        raise HTTPException(
                status_code=500,
                detail="AI malfunctioned. Or humanity did."
                )


