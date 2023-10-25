from sqlalchemy import Integer, Column, String, DateTime
from app.core.database import Base
from datetime import datetime


class Slider(Base):
    """
    Kelas ini mewakili tabel 'slider' dalam basis data.

    Atribut:
        slider_id (int): Kunci utama (primary key) untuk entitas slider.
        nama (str): Nama slider.
        image (str): URL gambar slider.

        created_at (datetime): Waktu pembuatan slider.
        updated_at (datetime, opsional): Waktu pembaruan slider (jika ada).

    Tabel 'slider' digunakan untuk menyimpan informasi slider dalam basis data.
    """

    __tablename__ = "slider"

    slider_id = Column(Integer, primary_key=True)
    nama = Column(String(length=255))
    image = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=True)
