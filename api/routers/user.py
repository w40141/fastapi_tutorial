from fastapi import APIRouter, Depends

import api.schemas.user as user_schema
from api.core.user import get_current_active_user

router = APIRouter()


@router.get("/users/me", response_model=user_schema.User)
async def read_users_me(current_user: user_schema.User = Depends(get_current_active_user)):
    return current_user


@router.get("/users/me/items")
async def read_own_items(current_user: user_schema.User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
