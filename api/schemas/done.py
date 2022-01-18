from pydantic.main import BaseModel


class DoneResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True
