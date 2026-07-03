from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.worker_schema import WorkerCreate, WorkerResponse
from app.services.worker_service import (
    create_worker,
    get_all_workers,
    get_worker,
)

router = APIRouter(
    prefix="/workers",
    tags=["Workers"]
)


@router.post("/", response_model=WorkerResponse)
def create(worker: WorkerCreate, db: Session = Depends(get_db)):
    return create_worker(worker, db)


@router.get("/", response_model=list[WorkerResponse])
def get_workers(db: Session = Depends(get_db)):
    return get_all_workers(db)


@router.get("/{worker_id}", response_model=WorkerResponse)
def get_worker_by_id(worker_id: int, db: Session = Depends(get_db)):
    worker = get_worker(worker_id, db)

    if worker is None:
        raise HTTPException(
            status_code=404,
            detail="Worker not found"
        )

    return worker