#!/bin/bash

# Render sets PORT automatically
PORT=${PORT:-8000}

# Start FastAPI with Uvicorn
uvicorn app.main:app --host 0.0.0.0 --port $PORT
