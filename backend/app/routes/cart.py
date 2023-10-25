from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.database.models.user import User
from app.core.token import get_currentUser
from app.repository.cart_repository import CartRepository
from app.service.cart_service import CartService
from app.domain.requests.cart.create import CartRequest
from app.domain.requests.cart.delete import DeleteCartSchema

cartrouter = APIRouter(prefix="/cart", tags=["Cart"])


@cartrouter.get("/")
def get_all_cart_user_id(
    db: Session = Depends(get_db), current_user: User = Depends(get_currentUser)
):
    try:
        cart_repository = CartRepository(db=db)
        cart_service = CartService(cart_repository=cart_repository)

        cart = cart_service.get_cart_items(user_id=current_user.user_id)

        return cart
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@cartrouter.post("/create")
def create_cart(
    request: CartRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_currentUser),
):
    try:
        cart_repository = CartRepository(db=db)
        cart_service = CartService(cart_repository=cart_repository)

        cart = cart_service.add_to_cart(
            name=request.name,
            price=request.price,
            image_product=request.image_product,
            quantity=request.quantity,
            weight=request.weight,
            product_id=request.product_id,
            user_id=current_user.user_id,
        )

        return cart
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@cartrouter.delete("/delete/{cart_id}")
def delete_cart(
    cart_id: int,
    current_user: User = Depends(get_currentUser),
    db: Session = Depends(get_db),
):
    try:
        cart_repository = CartRepository(db=db)
        cart_service = CartService(cart_repository=cart_repository)

        cart = cart_service.remove_from_cart(cart_id=cart_id)

        return cart
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@cartrouter.post("/delete-many")
def delete_cart_many(
    cart: DeleteCartSchema,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_currentUser),
):
    try:
        cart_repository = CartRepository(db=db)
        cart_service = CartService(cart_repository=cart_repository)

        cart = cart_service.remove_items_from_cart(cart_ids=cart.cartIds)

        return cart
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
