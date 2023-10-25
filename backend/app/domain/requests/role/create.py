from pydantic import BaseModel


class CreateRoleRequest(BaseModel):
    role: str
