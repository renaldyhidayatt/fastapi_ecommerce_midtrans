from pydantic import BaseModel


class UpdateUserRequest(BaseModel):
    id: int = None
    firstname: str
    lastname: str
    email: str
    role: int
    password: str
