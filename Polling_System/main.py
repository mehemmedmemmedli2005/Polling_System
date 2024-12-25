from fastapi import FastAPI
from app.routers import poll_router, vote_router

app = FastAPI()

# Register routers
app.include_router(poll_router.router, prefix="/polls", tags=["Polls"])
app.include_router(vote_router.router, prefix="/votes", tags=["Votes"])

@app.get("/")
def root():
    return {"message": "Welcome to the Polling System API"}
