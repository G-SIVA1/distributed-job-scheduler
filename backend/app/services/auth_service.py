from sqlalchemy.orm import Session

from app.auth.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.models.user import User
from app.schemas.user_schema import UserCreate


def register_user(user: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return None

    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(email: str, password: str, db: Session):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }