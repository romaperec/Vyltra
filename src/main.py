from fastapi import FastAPI

from src.auth.router import router as auth_router

app = FastAPI(
    title="Vyltra API 🐱‍👤",
    description="Vyltra — a modern platform for synchronized video watching and real-time communication. Connect with friends and create unforgettable moments together! ",
    version="1.0.0",
)
app.include_router(auth_router)


@app.get("/")
async def home():
    return {"Vyltra": "Working"}
