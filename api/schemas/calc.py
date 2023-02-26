from typing import Optional

from pydantic import BaseModel


class CalcStatus(BaseModel):
    id: str
    status: Optional[str] = None
    result: Optional[float] = None


class Sides(BaseModel):
    x: int
    y: int
