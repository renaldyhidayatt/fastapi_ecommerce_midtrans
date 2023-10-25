from pydantic import BaseModel


class UpdateSliderRequest(BaseModel):
    nama: str
    file_path: str
