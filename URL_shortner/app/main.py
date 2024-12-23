from fastapi import FastAPI
from app.routers.urls import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to url shortner app."}