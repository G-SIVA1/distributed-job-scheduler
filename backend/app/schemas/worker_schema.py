from pydantic import BaseModel


class WorkerCreate(BaseModel):
    name: str


class WorkerResponse(BaseModel):
    id: int
    name: str
    status: str
    is_active: bool

    class Config:
        from_attributes = True