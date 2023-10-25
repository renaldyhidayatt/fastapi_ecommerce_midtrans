from pydantic import BaseModel


class ReviewRequest(BaseModel):
    rating: int
    comment: str
