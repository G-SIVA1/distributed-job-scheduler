from sqlalchemy.orm import Session

from app.models.worker import Worker
from app.schemas.worker_schema import WorkerCreate


def create_worker(worker: WorkerCreate, db: Session):
    new_worker = Worker(
        name=worker.name
    )

    db.add(new_worker)
    db.commit()
    db.refresh(new_worker)

    return new_worker


def get_all_workers(db: Session):
    return db.query(Worker).all()


def get_worker(worker_id: int, db: Session):
    return db.query(Worker).filter(
        Worker.id == worker_id
    ).first()