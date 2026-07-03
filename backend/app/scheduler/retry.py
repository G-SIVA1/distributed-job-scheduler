from sqlalchemy.orm import Session

from app.models.job import Job

from app.scheduler.dead_letter import move_to_dead_letter

MAX_RETRIES = 3


def retry_job(job: Job, db: Session):
    if job.retry_count < MAX_RETRIES:
        job.retry_count += 1
        job.status = "QUEUED"

        db.commit()

        print(
            f"Retrying Job {job.id} "
            f"(Attempt {job.retry_count})"
        )

    else:
        move_to_dead_letter(job, db)