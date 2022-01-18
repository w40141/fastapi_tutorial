from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

import api.cruds.done as done_crud
from api.db.db import get_db
import api.schemas.done as done_scheme


router = APIRouter()


@router.put("/tasks/{task_id}/done", response_model=done_scheme.DoneResponse)
async def mark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_crud.get_done(db, task_id=task_id)
    if done is not None:
        raise HTTPException(status_code=404, detail="Done already exists")
    return await done_crud.create_done(db, task_id=task_id)


@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_crud.get_done(db, task_id=task_id)
    if done is None:
        raise HTTPException(status_code=404, detail="Done already exists")
    return await done_crud.delete_done(db, original=done)
