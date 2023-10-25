from pydantic import BaseModel


class UpdateCategoryRequest(BaseModel):
    id: int = None
    name: str
    file_path: str
