from fastapi import FastAPI
from app.api.routes import items, auth
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app with title from environment or default
app = FastAPI(title=os.getenv("APP_NAME", "FastAPI App"))

@app.get("/",tags=["SERVER"])
def root():
    """
    Root endpoint to verify the server is running.

    Returns:
        dict: A status message with the current environment and port.
    """
    env = os.getenv("APP_ENV", "development")
    port = os.getenv("APP_PORT", "8000")
    for key, value in os.environ.items():
        print(f"{key} = {value}")
    return {"message": f"{app.title} running in {env} mode on port {port}."}

# Register authentication and item management routes
app.include_router(auth.router)  
# Provides /token endpoint for JWT login
app.include_router(items.router, prefix="/items", tags=["Items"])
