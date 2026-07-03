from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.metrics_service import get_metrics

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"]
)


@router.get("/")
def metrics(db: Session = Depends(get_db)):
    return get_metrics(db)