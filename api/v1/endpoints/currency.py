from fastapi import APIRouter, Depends
# from schemas.currency import Currency

router = APIRouter()

@router.get("/")
def get_currencies():
    return {"message": "Welcome to my first root"}
