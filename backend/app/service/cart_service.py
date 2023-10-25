from app.domain.requests.cart.create import CartRequest

from .abstract_class.cart_abstract import CartServiceAbstract
from app.repository.abstract_class.cart_abstract import CartAbstractRepository


class CartService(CartServiceAbstract):
    def __init__(self, cart_repository: CartAbstractRepository):
        self.cart_repository = cart_repository

    def get_cart_items(self, user_id):
        return self.cart_repository.find_all_by_user_id(user_id=user_id)

    def add_to_cart(
        self,
        name: str,
        price: str,
        image_product: str,
        quantity: int,
        product_id: int,
        user_id: int,
        weight: int,
    ):
        cart_item = CartRequest(
            name=name,
            price=price,
            image_product=image_product,
            quantity=quantity,
            product_id=product_id,
            user_id=user_id,
            weight=weight,
        )
        return self.cart_repository.create(cart_item=cart_item)

    def remove_from_cart(self, cart_id):
        return self.cart_repository.delete(cart_id=cart_id)

    def remove_items_from_cart(self, cart_ids):
        return self.cart_repository.delete_many(cart_ids=cart_ids)
