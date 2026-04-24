from fastapi import FastAPI
from routes.analyze import router as analyze_router

app = FastAPI()

app.include_router(analyze_router)

@app.get("/")
def read_root():
    return {"message": "API working"}