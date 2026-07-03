from sqlalchemy.orm import Session

from app.models.job import Job
from app.models.queue import Queue
from app.models.worker import Worker


def get_metrics(db: Session):
    return {
        "total_jobs": db.query(Job).count(),
        "queued_jobs": db.query(Job).filter(Job.status == "QUEUED").count(),
        "running_jobs": db.query(Job).filter(Job.status == "RUNNING").count(),
        "completed_jobs": db.query(Job).filter(Job.status == "COMPLETED").count(),
        "dead_jobs": db.query(Job).filter(Job.status == "DEAD").count(),
        "total_queues": db.query(Queue).count(),
        "total_workers": db.query(Worker).count()
    }