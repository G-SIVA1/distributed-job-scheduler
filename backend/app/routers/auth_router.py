from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.schemas.token_schema import LoginRequest, Token
from app.services.auth_service import register_user, login_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = register_user(user, db)

    if new_user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return new_user


@router.post("/login", response_model=Token)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    token = login_user(
        request.email,
        request.password,
        db
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return token