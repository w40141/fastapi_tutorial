from typing import Optional

from pydantic import BaseModel, Field


class CalcBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")


class Tryangle(BaseModel):
    x: int
    y: int
