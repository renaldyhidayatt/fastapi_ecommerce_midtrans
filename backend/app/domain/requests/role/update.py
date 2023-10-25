from pydantic import BaseModel


class UpdateRoleRequest(BaseModel):
    role: str
