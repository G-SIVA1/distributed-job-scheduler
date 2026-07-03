from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.project_schema import ProjectCreate, ProjectResponse
from app.services.project_service import (
    create_project,
    get_all_projects,
    get_project_by_id,
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("/", response_model=ProjectResponse)
def create(project: ProjectCreate, db: Session = Depends(get_db)):
    return create_project(project, owner_id=1, db=db)


@router.get("/", response_model=list[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    return get_all_projects(db)


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = get_project_by_id(project_id, db)

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project