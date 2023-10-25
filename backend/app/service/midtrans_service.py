from uuid import uuid4
from app.core.midtrans import snap
from app.domain.requests.midtrans.create import MidtransRequest
from .abstract_class.midtrans_abstract import MidtransAbstractService


class MidtransService(MidtransAbstractService):
    @staticmethod
    def createTransaction(dto: MidtransRequest):
        try:
            parameter = {
                "transaction_details": {
                    "order_id": "order-csb-" + str(uuid4()),
                    "gross_amount": dto.gross_amount,
                },
                "credit_card": {
                    "secure": False,
                },
                "customer_details": {
                    "first_name": dto.firstname,
                    "last_name": dto.lastname,
                    "email": dto.email,
                    "phone": dto.phone,
                },
                "callbacks": {
                    "finish": "http://localhost:3000/user/order",
                },
            }

            return snap.create_transaction(parameters=parameter)
        except Exception as e:
            raise Exception(f"Failed to create transaction: {str(e)}")
