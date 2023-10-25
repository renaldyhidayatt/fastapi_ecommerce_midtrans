from pydantic import BaseModel


class OngkosRequest(BaseModel):
    asal: str
    tujuan: str
    berat: int
    kurir: str
