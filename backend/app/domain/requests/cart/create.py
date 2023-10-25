from pydantic import BaseModel


class CartRequest(BaseModel):
    name: str
    price: str
    image_product: str
    quantity: int
    product_id: int
    user_id: int = None
    weight: int
