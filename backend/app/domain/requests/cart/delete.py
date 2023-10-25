from pydantic import BaseModel
from typing import List


class DeleteCartSchema(BaseModel):
    cartIds: List[int]
