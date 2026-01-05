from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agents.agent_runner import run_agent

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.post("/agent2/analyze")
def analyze(request: QueryRequest):
    """
    Entry point for Agent-2.
    IMPORTANT:
    - extract_intent is called ONLY inside AgentRunner
    - API passes ONLY the raw query string
    """
    try:
        return run_agent(request.query)  # ✅ STRING ONLY
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
