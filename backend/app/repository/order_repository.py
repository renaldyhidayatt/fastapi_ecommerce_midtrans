from sqlalchemy.orm import Session
from .abstract_class.order_abstract import OrderAbstractRepository
from app.database.models.order import Order, OrderItems, ShippingAddress
from app.domain.requests.order.create import CreateOrderRequest
from app.database.models.user import User
from uuid import uuid4


class OrderRepository(OrderAbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        try:
            return self.session.query(Order).all()
        except Exception as e:
            raise e

    def create_order(self, request: CreateOrderRequest, current_user: User):
        try:
            order_create = Order(
                user_id=current_user.user_id,
                name=request.name,
                phone=request.phone,
                courier=request.courier,
                email=current_user.email,
                shipping_method=request.shippingMethod,
                shipping_cost=request.shippingCost,
                total_product=request.totalProduct,
                total_price=request.totalPrice,
                transactionId=str(uuid4()),  # Convert to string
            )
            self.session.add(order_create)
            self.session.commit()

            db_order = (
                self.session.query(Order)
                .filter(Order.order_id == order_create.order_id)
                .first()
            )
            shipping_a = ShippingAddress(
                alamat=request.shippingAddress.alamat,
                kota=request.shippingAddress.kota,
                negara=request.shippingAddress.negara,
                provinsi=request.shippingAddress.provinsi,
                order_id=db_order.order_id,
            )
            self.session.add(shipping_a)

            for item in request.cartItems:
                order_item = OrderItems(
                    name=item.name,
                    quantity=int(item.quantity),
                    price=int(item.price),
                    order_id=db_order.order_id,
                )

                self.session.add(order_item)
                self.session.commit()
                self.session.refresh(order_item)

            self.session.commit()
            self.session.refresh(shipping_a)

            return order_create

        except Exception as e:
            raise e

    def order_by_id(self, order_id):
        try:
            order = self.session.query(Order).filter(Order.order_id == order_id).first()

            response = {
                "id": order.order_id,
                "user_id": order.user_id,
                "name": order.name,
                "phone": order.phone,
                "email": order.email,
                "shippingMethod": order.shipping_method,
                "shippingCost": order.shipping_cost,
                "totalProduct": order.total_product,
                "totalPrice": order.total_price,
                "transactionId": order.transactionId,
                "created_at": order.created_at,
                "updated_at": order.updated_at,
                "order_items": order.order_items,
                "shipping_address": order.shipping_address,
            }

            return response
        except Exception as e:
            raise e

    def order_by_user(self, user_id):
        return self.session.query(Order).filter_by(user_id=user_id).all()
