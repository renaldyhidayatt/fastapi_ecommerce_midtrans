from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.core.token import (
    create_access_token,
    get_currentUser,
    verify_token,
    create_refresh_token,
)
from app.core.database import get_db
from app.core.hashing import Hashing
from sqlalchemy.orm import Session
from app.domain.requests.auth.refresh_token import RefreshTokenRequest
from app.domain.requests.user.create import CreateUserRequest
from app.service.auth_service import AuthService
from app.repository.user_repository import UserRepository

authrouter = APIRouter(prefix="/auth", tags=["Authentication"])


@authrouter.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = UserRepository(session=db)

    auth = AuthService(user_repository=user)

    auth_email = auth.login_user(email=request.username)

    if not auth_email:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials "
        )

    if not Hashing.verify(auth_email.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password"
        )

    access_token = create_access_token(data={"sub": auth_email.email})
    refresh_token = create_refresh_token(data={"sub": auth_email.email})
    response = {
        "id": auth_email.user_id,
        "firstname": auth_email.firstname,
        "lastname": auth_email.lastname,
        "email": auth_email.email,
        "access_token": access_token,
        "refresh_token": refresh_token,
    }

    return response


@authrouter.post("/refresh-token")
async def refresh_access_token(
    refresh_token: RefreshTokenRequest,
    db: Session = Depends(get_db),
    current_user: Session = Depends(get_currentUser),
):
    try:
        user = verify_token(token=refresh_token.refresh_token, db=db)

        if user:
            access_token = create_access_token(data={"sub": user.email})

            return {"access_token": access_token}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid refresh token")


@authrouter.post("/register")
def create_user(
    request: CreateUserRequest,
    db: Session = Depends(get_db),
):
    try:
        user_repository = UserRepository(session=db)
        user_service = AuthService(user_repository=user_repository)

        user = user_service.register_user(
            request.firstname, request.lastname, request.email, request.password
        )
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
