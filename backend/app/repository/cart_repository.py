from .abstract_class.cart_abstract import CartAbstractRepository
from sqlalchemy.orm import Session
from app.database.models.cart import Cart
from app.domain.requests.cart.create import CartRequest


class CartRepository(CartAbstractRepository):
    def __init__(self, db: Session):
        self.db = db

    def find_all_by_user_id(self, user_id):
        try:
            return self.db.query(Cart).filter(Cart.user_id == user_id).all()
        except Exception as e:
            raise e

    def create(self, cart_item: CartRequest):
        try:
            cart = Cart(
                name=cart_item.name,
                price=cart_item.price,
                image=cart_item.image_product,
                quantity=cart_item.quantity,
                weight=cart_item.weight,
                product_id=cart_item.product_id,
                user_id=cart_item.user_id,
            )

            self.db.add(cart)
            self.db.commit()
            self.db.refresh(cart)
            return cart_item
        except Exception as e:
            raise e

    def delete(self, cart_id):
        try:
            cart_item = self.db.query(Cart).filter(Cart.cart_id == cart_id).first()
            if cart_item:
                self.db.delete(cart_item)
                self.db.commit()
                return True
            return False
        except Exception as e:
            raise e

    def delete_many(self, cart_ids):
        try:
            deleted_count = (
                self.db.query(Cart)
                .filter(Cart.cart_id.in_(cart_ids))
                .delete(synchronize_session=False)
            )
            self.db.commit()
            return deleted_count
        except Exception as e:
            raise e
