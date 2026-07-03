from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from app.models.base import Base


class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    status = Column(String(30), default="IDLE")

    heartbeat = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )