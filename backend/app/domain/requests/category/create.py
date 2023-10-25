from pydantic import BaseModel


class CreateCategoryRequest(BaseModel):
    name: str
    file_path: str
