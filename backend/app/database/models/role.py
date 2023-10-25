from sqlalchemy import Integer, Column, String, DateTime
from app.core.database import Base
from datetime import datetime


class Role(Base):
    """
    Kelas ini mewakili tabel 'role' dalam basis data.

    Atribut:
        role_id (int): Kunci utama (primary key) untuk entitas peran (role).
        role (str): Nama peran (role).

        created_at (datetime): Waktu pembuatan peran.
        updated_at (datetime, opsional): Waktu pembaruan peran (jika ada).

    Tabel 'role' digunakan untuk menyimpan informasi peran (role) dalam basis data.
    """

    __tablename__ = "role"

    role_id = Column(Integer, primary_key=True)
    name = Column(String(length=128))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=True)
