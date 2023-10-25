from pydantic import BaseModel


class RegisterRequest(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
