from pydantic import BaseModel


class UpdateProductRequest(BaseModel):
    name: str
    category_id: str
    description: str
    price: int
    countInStock: int
    weight: int
    rating: int
    brand: str
    file_path: str
