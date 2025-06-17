from fastapi import FastAPI
from app.api.routes import items
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "FastAPI App"))

@app.get("/")
def root():
    """
    Home route to confirm server is running.
    """
    env = os.getenv("APP_ENV", "development")
    port = os.getenv("APP_PORT", "8000")
    return {"message": f"✅ {app.title} running in {env} mode on port {port}."}

app.include_router(items.router, prefix="/items", tags=["Users"])
