import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI(title="Mini AI Interview Screener", version="1.0")


# ===== MODELS =====
class AnswerRequest(BaseModel):
    text: str


class RankRequest(BaseModel):
    answers: list[str]


# ===== HELPER FUNCTION =====
async def evaluate_text(text: str):
    prompt = f"""
You are an interview evaluator. Analyze the candidate’s answer.

Answer: {text}

Return ONLY a valid JSON object:
{{
  "score": 1-5,
  "summary": "one line summary",
  "improvement": "one improvement advice"
}}
Make sure the response is STRICT JSON.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        raw = response.choices[0].message.content
        return json.loads(raw)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")


# ===== ROUTES =====

@app.post("/evaluate-answer")
async def evaluate_answer(req: AnswerRequest):
    return await evaluate_text(req.text)


@app.post("/rank-candidates")
async def rank_candidates(req: RankRequest):
    results = []

    for ans in req.answers:
        evaluated = await evaluate_text(ans)
        results.append({
            "answer": ans,
            "score": evaluated["score"],
            "summary": evaluated["summary"],
            "improvement": evaluated["improvement"]
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return {"ranked": results}
