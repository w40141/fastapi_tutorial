from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()


@router.get("/items")
async def read_items(token: str = Depends(outh2_scheme)):
    return {"token": token}
