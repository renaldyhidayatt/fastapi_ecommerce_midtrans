from app.database.models.user import User
from app.domain.requests.order.create import CreateOrderRequest
from .abstract_class.order_abstract import OrderAbstractService
from app.repository.abstract_class.order_abstract import OrderAbstractRepository


class OrderService(OrderAbstractService):
    def __init__(self, order_repository: OrderAbstractRepository):
        self.order_repository = order_repository

    def get_all(self):
        return self.order_repository.get_all()

    def create_order(self, request: CreateOrderRequest, current_user: User):
        return self.order_repository.create_order(
            request=request, current_user=current_user
        )

    def order_by_id(self, order_id: int):
        return self.order_repository.order_by_id(order_id=order_id)

    def order_by_user(self, user_id):
        return self.order_repository.order_by_user(user_id=user_id)
