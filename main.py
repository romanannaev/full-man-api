from fastapi import FastAPI

from api.v1.endpoints import currency

app = FastAPI()

app.include_router(currency.router, prefix="/currencies", tags=["currencies"])

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI application!"}
