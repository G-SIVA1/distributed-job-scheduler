from sqlalchemy.orm import Session

from app.models.job import Job
from app.schemas.job_schema import JobCreate


def create_job(job: JobCreate, db: Session):
    new_job = Job(
        name=job.name,
        payload=job.payload,
        priority=job.priority,
        queue_id=job.queue_id,
        scheduled_at=job.scheduled_at,
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


def get_all_jobs(db: Session):
    return db.query(Job).all()


def get_job_by_id(job_id: int, db: Session):
    return db.query(Job).filter(Job.id == job_id).first()