from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project_schema import ProjectCreate


def create_project(project: ProjectCreate, owner_id: int, db: Session):
    new_project = Project(
        name=project.name,
        description=project.description,
        owner_id=owner_id
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


def get_all_projects(db: Session):
    return db.query(Project).all()


def get_project_by_id(project_id: int, db: Session):
    return db.query(Project).filter(Project.id == project_id).first()