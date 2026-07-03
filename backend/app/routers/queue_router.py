from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.queue_schema import QueueCreate, QueueResponse
from app.services.queue_service import (
    create_queue,
    get_all_queues,
    get_queue_by_id,
    pause_queue,
    resume_queue,
)

router = APIRouter(
    prefix="/queues",
    tags=["Queues"]
)


@router.post("/", response_model=QueueResponse)
def create(queue: QueueCreate, db: Session = Depends(get_db)):
    return create_queue(queue, db)


@router.get("/", response_model=list[QueueResponse])
def get_queues(db: Session = Depends(get_db)):
    return get_all_queues(db)


@router.get("/{queue_id}", response_model=QueueResponse)
def get_queue(queue_id: int, db: Session = Depends(get_db)):
    queue = get_queue_by_id(queue_id, db)

    if queue is None:
        raise HTTPException(
            status_code=404,
            detail="Queue not found"
        )

    return queue


@router.patch("/{queue_id}/pause", response_model=QueueResponse)
def pause(queue_id: int, db: Session = Depends(get_db)):
    queue = pause_queue(queue_id, db)

    if queue is None:
        raise HTTPException(
            status_code=404,
            detail="Queue not found"
        )

    return queue


@router.patch("/{queue_id}/resume", response_model=QueueResponse)
def resume(queue_id: int, db: Session = Depends(get_db)):
    queue = resume_queue(queue_id, db)

    if queue is None:
        raise HTTPException(
            status_code=404,
            detail="Queue not found"
        )

    return queue