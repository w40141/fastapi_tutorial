from fastapi import APIRouter

import api.schemas.calc as calc_scheme
from api.core.celery import celery, pythagorean_theorem

router = APIRouter()


@router.post(
    "/calc",
    response_model=calc_scheme.CalcStatus,
    response_model_exclude_unset=True,
)
async def post_calc(sides: calc_scheme.Sides):
    task = pythagorean_theorem.delay(x=sides.x, y=sides.y)
    return calc_scheme.CalcStatus(id=task.id)


@router.get("/calc/{calc_id}", response_model=calc_scheme.CalcStatus)
async def get_result(calc_id: str):
    result = celery.AsyncResult(calc_id)
    status = calc_scheme.CalcStatus(
        id=calc_id, status=result.status, result=result.result
    )
    return status
