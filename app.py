from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from evaluator.scorer import LLMScorer

load_dotenv()

scorer = LLMScorer()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EvaluateRequest(BaseModel):
    question: str
    response: str

@app.post("/evaluate")
async def evaluate(request: EvaluateRequest):
    result = scorer.evaluate(request.question, request.response)
    return result