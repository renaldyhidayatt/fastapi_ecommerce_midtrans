from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repository.user_repository import UserRepository
from app.service.user_service import UserService
from app.domain.requests.user.create import CreateUserRequest
from app.domain.requests.user.update import UpdateUserRequest
from app.core.token import get_currentUser


user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    try:
        user_repository = UserRepository(session=db)
        user_service = UserService(user_repository=user_repository)

        users = user_service.get_all_users()

        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@user_router.get("/{email}")
def get_user_by_id(email: str, db: Session = Depends(get_db)):
    try:
        user_repository = UserRepository(session=db)
        user_service = UserService(user_repository=user_repository)

        user = user_service.get_user_by_email(email=email)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@user_router.post("/create")
def create_user(
    request: CreateUserRequest,
    db: Session = Depends(get_db),
):
    try:
        user_repository = UserRepository(session=db)
        user_service = UserService(user_repository=user_repository)

        user = user_service.create_user(
            request.firstname, request.lastname, request.email, request.password
        )
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@user_router.put("/update/{user_id}")
def update_user(
    user_id: int, request: UpdateUserRequest, db: Session = Depends(get_db)
):
    try:
        user_repository = UserRepository(session=db)
        user_service = UserService(user_repository=user_repository)

        user = user_service.update_user(
            user_id,
            request.firstname,
            request.lastname,
            request.email,
            request.password,
        )
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@user_router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user_repository = UserRepository(session=db)
        user_service = UserService(user_repository=user_repository)

        user_service.delete_user(user_id)
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
