from sqlalchemy.orm import Session

from app.models.queue import Queue
from app.schemas.queue_schema import QueueCreate


def create_queue(queue: QueueCreate, db: Session):
    new_queue = Queue(
        name=queue.name,
        priority=queue.priority,
        concurrency_limit=queue.concurrency_limit,
        project_id=queue.project_id
    )

    db.add(new_queue)
    db.commit()
    db.refresh(new_queue)

    return new_queue


def get_all_queues(db: Session):
    return db.query(Queue).all()


def get_queue_by_id(queue_id: int, db: Session):
    return db.query(Queue).filter(Queue.id == queue_id).first()


def pause_queue(queue_id: int, db: Session):
    queue = db.query(Queue).filter(Queue.id == queue_id).first()

    if queue:
        queue.is_paused = True
        db.commit()
        db.refresh(queue)

    return queue


def resume_queue(queue_id: int, db: Session):
    queue = db.query(Queue).filter(Queue.id == queue_id).first()

    if queue:
        queue.is_paused = False
        db.commit()
        db.refresh(queue)

    return queue