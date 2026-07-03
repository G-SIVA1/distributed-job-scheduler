import random
import time

from sqlalchemy.orm import Session

from app.models.job import Job
from app.scheduler.retry import retry_job


def execute_job(job: Job, db: Session):
    print(f"Executing Job {job.id}")

    job.status = "RUNNING"
    db.commit()

    time.sleep(5)

    # Simulate random success/failure
    success = random.choice([True, False])

    if success:
        job.status = "COMPLETED"
        db.commit()

        print(f"Job {job.id} completed")

    else:
        print(f"Job {job.id} failed")

        retry_job(job, db)