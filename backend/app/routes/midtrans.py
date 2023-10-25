from fastapi import APIRouter
from app.service.midtrans_service import MidtransService
from app.domain.requests.midtrans.create import MidtransRequest

midtransrouter = APIRouter(prefix="/midtrans", tags=["Midtrans"])


@midtransrouter.post("/transaction")
def create_transaction(dto: MidtransRequest):
    return MidtransService.createTransaction(dto=dto)
