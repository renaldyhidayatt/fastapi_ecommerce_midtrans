from pydantic import BaseModel
from typing import List


class CartItemRequest(BaseModel):
    name: str
    quantity: int
    price: int


class ShippingAddressRequest(BaseModel):
    alamat: str
    provinsi: str
    kota: str
    negara: str


class CreateOrderRequest(BaseModel):
    name: str
    phone: str
    courier: str
    shippingAddress: ShippingAddressRequest
    cartItems: List[CartItemRequest]
    shippingMethod: str
    shippingCost: int
    totalProduct: str
    totalPrice: str
