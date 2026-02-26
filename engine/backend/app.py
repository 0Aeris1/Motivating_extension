from fastapi import FastAPI, HTTPException, Request # FastAPI core classes
from fastapi.middleware.cors import CORSMiddleware # Middleware for cross-origin requests
from fastapi.responses import JSONResponse # Custom JSON responses
from slowapi import Limiter # Rate limiting
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address # Identify client IP for limiter

from engine.backend.ai import generate_motivation # AI function for motivational messages
from engine.backend.schemas import MotivationRequest, MotivationResponse # Request/response models

# Initialise rate limiter using client's IP address
limiter = Limiter(key_func=get_remote_address)

# Create FastAPI app instance
app = FastAPI()
app.state.limiter = limiter # attach limiter to app state

# Customer handler for rate limit exceeded
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
                status_code=429, # Too many requests
                content={"detail": "Slow down. Discipline builds greatness."}
            )

# Enable CORS so frontend (extension) can communicate with backend
app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"], # allow all domains
        allow_methods = ["*"], # allow all HTTP methods
        allow_headers = ["*"], # allow all headers
allow_credentials = True
        )

# Endpoint to get motivational message
@app.post("/motivate", response_model=MotivationResponse)
@limiter.limit("5/day") # limit each IP to 5 requests per day
async def motivate(request: Request, req: MotivationRequest):
    try:
        reply = generate_motivation(req.text) # generate motivational text
        return {"response": reply}
    except HTTPException:
        raise # re-raise knwon HTTP errors
    except Exception as e:
        print("ERROR:", e)   # log unexpected errors
        # Return generic 500 error to client
        raise HTTPException(
            status_code=500,
            detail="AI malfunctioned. Or humanity did."
        )
