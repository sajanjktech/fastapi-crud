from fastapi import FastAPI
from app.api.routes import items, auth
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "FastAPI App"))

# Root endpoint
@app.get("/", tags=["Server"])
def root():
    env = os.getenv("APP_ENV", "development")
    port = os.getenv("APP_PORT", "8000")
    return {"message": f"{app.title} running in {env} mode on port {port}."}

#API routes
app.include_router(auth.router) 
app.include_router(items.router, prefix="/items", tags=["Items"]) 
    