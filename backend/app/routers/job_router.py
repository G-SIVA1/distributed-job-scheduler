from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.job_schema import JobCreate, JobResponse
from app.services.job_service import (
    create_job,
    get_all_jobs,
    get_job_by_id,
)

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post("/", response_model=JobResponse)
def create(job: JobCreate, db: Session = Depends(get_db)):
    return create_job(job, db)


@router.get("/", response_model=list[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    return get_all_jobs(db)


@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = get_job_by_id(job_id, db)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return job