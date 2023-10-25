from pydantic import BaseModel


class MidtransRequest(BaseModel):
    gross_amount: int
    firstname: str
    lastname: str
    email: str
    phone: str
