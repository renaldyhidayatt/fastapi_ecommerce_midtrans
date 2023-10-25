from pydantic import BaseModel
from typing import Optional


class CreateProductRequest(BaseModel):
    name: str
    category_id: str
    description: str
    price: int
    countInStock: int
    weight: int
    rating: Optional[int]
    file_path: str
