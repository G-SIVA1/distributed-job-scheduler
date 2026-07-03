from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.models.base import Base


class Queue(Base):
    __tablename__ = "queues"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    priority = Column(Integer, default=1)

    concurrency_limit = Column(Integer, default=1)

    is_paused = Column(Boolean, default=False)

    project_id = Column(
        Integer,
        ForeignKey("projects.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )