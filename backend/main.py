from fastapi import FastAPI
from models import init_db

init_db()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI Backend is Running!"}
