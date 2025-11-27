import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq
import json
import re

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI(title="Mini AI Interview Screener", version="0.2.0")


# MODELS
class AnswerRequest(BaseModel):
    text: str

class RankRequest(BaseModel):
    answers: list[str]


# Clean JSON helper (handles cases where model adds extra text)
def extract_json(text: str):
    try:
        json_str = re.search(r"\{.*\}", text, re.DOTALL)
        if not json_str:
            raise Exception("No JSON found in response")
        return json.loads(json_str.group())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invalid JSON from LLM: {e}")


# Evaluate helper
async def evaluate_text(text: str):
    prompt = f"""
Return ONLY a JSON object. No markdown, no explanation.

Evaluate the following interview answer:

Answer: "{text}"

Respond exactly in this JSON format:
{{
  "score": 1-5,
  "summary": "short summary",
  "improvement": "one improvement"
}}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        raw = response.choices[0].message.content
        return extract_json(raw)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")


# ROUTES
@app.post("/evaluate-answer")
async def evaluate_answer(req: AnswerRequest):
    return await evaluate_text(req.text)


@app.post("/rank-candidates")
async def rank_candidates(req: RankRequest):
    results = []

    for ans in req.answers:
        eval_data = await evaluate_text(ans)
        results.append({
            "answer": ans,
            "score": eval_data["score"],
            "summary": eval_data["summary"],
            "improvement": eval_data["improvement"]
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return {"ranked": results}
