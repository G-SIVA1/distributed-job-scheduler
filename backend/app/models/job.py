from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.sql import func

from app.models.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    payload = Column(JSON, nullable=True)

    status = Column(String(30), default="QUEUED")

    priority = Column(Integer, default=1)

    retry_count = Column(Integer, default=0)

    scheduled_at = Column(DateTime(timezone=True), nullable=True)

    queue_id = Column(
        Integer,
        ForeignKey("queues.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )