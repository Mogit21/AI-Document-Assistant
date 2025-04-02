from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Document Assistant")

# Include API routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "AI Document Assistant is running!"}
