from fastapi import FastAPI
from app.routes import prediction

app = FastAPI()

app.include_router(prediction.router)


@app.get("/")
def home():
    return {
        "message": "API running"
    }