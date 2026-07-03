from sqlalchemy.orm import Session

from app.models.job import Job


def move_to_dead_letter(job: Job, db: Session):
    job.status = "DEAD"

    db.commit()

    print(f"Job {job.id} moved to Dead Letter Queue")