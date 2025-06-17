from fastapi import FastAPI
from pydantic import BaseModel
from app.api.routes import items

app = FastAPI()


@app.get("/")
def root():
    """
    Home route to confirm server is running.
    """
    return {"message": "✅ Server running at http://127.0.0.1:8000/"}

app.include_router(items.router , prefix = "/items" , tags = ["Users"])