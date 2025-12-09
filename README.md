# interview-screener   check it out ->  https://interview-screener-f1q0.onrender.com/docs
Mini AI Interview Screener using FastAPI
🚀 Mini AI Interview Screener (Backend Only)

A lightweight backend service built for the 48-Hour Real-World Build Challenge by Airevo Labs.
This project evaluates candidate answers using an LLM and provides structured, consistent scoring.

🧩 Real-Time Usefulness of This AI Mini Interview Screener

This Mini AI Interview Screener is not just an assignment — it replicates what modern hiring teams actually need. Here’s how it becomes valuable in real-world recruitment pipelines:

✅ 1. Automated First-Round Screening

Hiring teams often receive hundreds of applications per role. Manually reading every answer is slow and inconsistent.
This API instantly evaluates candidate responses, giving:

A score (1–5)

A concise summary

One improvement suggestion

This allows recruiters to filter strong candidates within seconds instead of hours, increasing overall efficiency.

✅ 2. Consistent, Unbiased Evaluation

Human reviewers can be affected by bias, fatigue, or mood.
Your LLM-powered scoring applies the same criteria every time, leading to:

Fairer evaluations

More objective comparisons

Higher-quality shortlisting

This is especially useful for large hiring drives or campus recruitment.

✅ 3. Fast Ranking of Multiple Candidates

With the /rank-candidates endpoint, teams can submit dozens or hundreds of responses at once.

The system returns a sorted list from best to worst, enabling:

Quick shortlisting

Automated pipeline progression

Instant insights into candidate performance

This is ideal for high-volume hiring and hackathon-style evaluations.

✅ 4. Works Seamlessly With Any Hiring System

Since it uses Groq’s LLaMA API (extremely fast + cost-efficient), the screener can plug directly into:

ATS systems

Recruiter dashboards

Career portals

Internal HR tools

No need to modify the backend — the LLM logic is modular and reusable.

✅ 5. Supports All Job Types

This screener can evaluate answers for:

Behavioral questions

Technical reasoning

Communication skills

Problem-solving explanations

Its flexibility makes it useful across both tech and non-tech hiring.

✅ 6. Real-Time Candidate Feedback

It can also serve as a training tool for job seekers:

Candidates enter answers

They instantly get feedback + improvement suggestions

This transforms the system into an AI-based learning and preparation platform.

✅ 7. Foundation for a Full AI Interview System

Your backend can easily scale into a complete intelligent hiring system, including:

Automated follow-up questions

Multi-round screening

Voice/video analysis

Resume-based question generation

Behavioral scoring

This makes your solution not just functional—but scalable and future-ready.

📌 Features
✅ /evaluate-answer

Accepts:

{ "answer": "Candidate says: <their answer>" }


Returns:

{
  "score": 1-5,
  "summary": "One-line summary",
  "improvement": "One improvement suggestion"
}

✅ /rank-candidates

Accepts an array of candidate answers

Scores each using the LLM

Returns candidates sorted from highest score → lowest

⚡ Powered by Groq (LLaMA 3.1)

Ultra-fast inference

Cost-efficient

Reliable for structured response generation

🧠 Technology Choices & Why
FastAPI (Python)

Extremely fast (built on ASGI + Uvicorn)

Automatic interactive docs (/docs)

Clean request/response validation with Pydantic

Perfect for building small but scalable production APIs

Groq API (LLaMA 3.1)

Selected because:

Fast inference → ideal for real-time interview evaluation

High accuracy + low latency

Simple JSON-based API integration

Free tier suitable for rapid prototyping

Works well for deterministic structured outputs

Why This Stack?

This assignment tests:

LLM integration

Clean API design

Ability to build fast & ship quickly
FastAPI + Groq provides the perfect balance of speed, clarity, cost-efficiency, and production readiness.

📂 Project Structure

├── app
│   ├── main.py          # FastAPI app + API routes
├── start.sh             # Render startup script
├── requirements.txt
└── README.md

🔧 Setup Instructions
1. Clone the repository
git clone <your-repo-url>
cd <your-project-folder>

2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Add your Groq API key

Create a .env file:

GROQ_API_KEY=gsk_key
5. Run the server
uvicorn app.main:app --reload
Server runs at:
👉 http://localhost:8000
Interactive Swagger docs:
👉 http://localhost:8000/docs

🌐 Live Deployment (Render)

This backend is deployed on Render for easy testing and real-time evaluation.

🔗 Live API Base URL:
https://interview-screener-f1q0.onrender.com/

You can directly test the APIs via:

🔹 Swagger UI (Interactive Docs)

👉 https://interview-screener-f1q0.onrender.com/docs

🧪 API Testing Examples

Test /evaluate-answer

POST → /evaluate-answer

Body:

{
  "answer": "Candidate says: I have 3 years of experience working with APIs..."
}


Example Output:

{
  "score": 4,
  "summary": "Candidate highlights relevant API experience.",
  "improvement": "Add a specific example to strengthen the answer."
}

Test /rank-candidates

POST → /rank-candidates

Body:

{
  "answers": [
    "Candidate says: I led a backend team...",
    "Candidate says: I like coding.",
    "Candidate says: I built multiple API systems using FastAPI..."
  ]
}


Output:

{
  "ranked_candidates": [
    {
      "score": 5,
      "answer": "Candidate says: I built multiple API systems using FastAPI..."
    },
    {
      "score": 4,
      "answer": "Candidate says: I led a backend team..."
    },
    {
      "score": 2,
      "answer": "Candidate says: I like coding."
    }
  ]
}

📽 Loom Walkthrough (2–3 Minutes)
Link: 
https://drive.google.com/file/d/1CeVgiope2sOQyDR4UtVIF_b2bQK_PA7Y/view?usp=drivesdk
Git Repo link:
https://github.com/ChanduPulluru/interview-screener

This project is intentionally clean, simple, and production-ready — focused on:

LLM integration

Reliable structured responses

Fast and readable API design
