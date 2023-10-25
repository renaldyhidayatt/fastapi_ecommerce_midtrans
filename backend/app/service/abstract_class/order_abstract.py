from abc import ABC, abstractmethod
from app.domain.requests.order.create import CreateOrderRequest
from app.database.models.user import User


class OrderAbstractService(ABC):
    @abstractmethod
    def get_all(self):
        """Get all orders."""
        pass

    @abstractmethod
    def create_order(self, request: CreateOrderRequest, current_user: User):
        """Create a new order."""
        pass

    @abstractmethod
    def order_by_id(self, order_id):
        """Get an order by its ID."""
        pass

    @abstractmethod
    def order_by_user(self, user_id):
        """Get orders for a specific user."""
        pass
