from pydantic import BaseModel


class CreateSliderRequest(BaseModel):
    nama: str
    file_path: str
