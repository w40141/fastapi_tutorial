from typing import List

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.task as task_curd
import api.schemas.task as task_schema
from api.db.db import get_db

router = APIRouter()


@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return await task_curd.get_tasks_with_done(db)


@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)):
    return await task_curd.create_task(db, task_body)


@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)):
    task = await task_curd.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not Found")
    return await task_curd.update_task(db, task_body, original=task)


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await task_curd.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not Found")
    return await task_curd.delete_task(db, original=task)
