import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI(title="Mini AI Interview Screener", version="0.1.0")


# REQUEST MODELS
class AnswerRequest(BaseModel):
    text: str

class RankRequest(BaseModel):
    answers: list[str]


# HELPER
async def evaluate_text(text: str):
    try:
        prompt = f"""
You are an interview evaluator. Analyze the candidate's answer.

Answer: {text}

Return a JSON object ONLY with:
- score (1-5)
- summary
- improvement
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # ✅ VALID GROQ MODEL
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        content = response.choices[0].message.content

        return json.loads(content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")


# ROUTES
@app.post("/evaluate-answer")
async def evaluate_answer(req: AnswerRequest):
    return await evaluate_text(req.text)


@app.post("/rank-candidates")
async def rank_candidates(req: RankRequest):
    ranked = []

    for ans in req.answers:
        result = await evaluate_text(ans)
        ranked.append({
            "answer": ans,
            "score": result["score"],
            "summary": result["summary"],
            "improvement": result["improvement"]
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)

    return {"ranked": ranked}
