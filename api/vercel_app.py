from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI backend on Vercel"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

# Vercel-specific handler
if os.getenv("VERCEL"):
    from mangum import Mangum
    handler = Mangum(app)
