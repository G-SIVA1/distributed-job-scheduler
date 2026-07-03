from pydantic import BaseModel


class QueueCreate(BaseModel):
    name: str
    priority: int = 1
    concurrency_limit: int = 1
    project_id: int


class QueueResponse(BaseModel):
    id: int
    name: str
    priority: int
    concurrency_limit: int
    is_paused: bool
    project_id: int

    class Config:
        from_attributes = True