import threading
import time

from app.database.database import SessionLocal
from app.models.job import Job

from app.scheduler.executor import execute_job


def scheduler_loop():
    while True:

        db = SessionLocal()

        job = (
            db.query(Job)
            .filter(Job.status == "QUEUED")
            .order_by(Job.priority.desc())
            .first()
        )

        if job:
            execute_job(job, db)

        db.close()

        time.sleep(3)


def start_scheduler():
    thread = threading.Thread(
        target=scheduler_loop,
        daemon=True
    )

    thread.start()