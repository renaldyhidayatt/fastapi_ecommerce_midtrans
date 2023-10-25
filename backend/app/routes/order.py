from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.token import get_currentUser
from app.database.models.user import User
from app.core.database import get_db
from app.domain.requests.order.create import CreateOrderRequest
from app.repository.order_repository import OrderRepository
from app.service.order_service import OrderService


orderrrouter = APIRouter(prefix="/order", tags=["Order"])


@orderrrouter.get("/")
def get_all(db: Session = Depends(get_db)):
    try:
        order_repository = OrderRepository(session=db)

        order_service = OrderService(order_repository=order_repository)

        return order_service.get_all()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@orderrrouter.post("/create")
def create_order(
    request: CreateOrderRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_currentUser),
):
    try:
        order_repository = OrderRepository(session=db)

        order_service = OrderService(order_repository=order_repository)

        return order_service.create_order(request=request, current_user=current_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@orderrrouter.get("/orderbyuser")
def order_by_user(
    db: Session = Depends(get_db), current_user: User = Depends(get_currentUser)
):
    try:
        order_repository = OrderRepository(session=db)

        order_service = OrderService(order_repository=order_repository)

        return order_service.order_by_user(user_id=current_user.user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@orderrrouter.get("/orderbyid/{id}")
def order_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_currentUser),
):
    try:
        order_repository = OrderRepository(session=db)

        order_service = OrderService(order_repository=order_repository)

        return order_service.order_by_id(order_id=id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
