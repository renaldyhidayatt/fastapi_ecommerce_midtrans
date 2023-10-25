from sqlalchemy import Integer, Column, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from app.core.database import Base


class Category(Base):
    """
    Kelas ini mewakili tabel 'category' dalam basis data.

    Atribut:
        category_id (int): Kunci utama (primary key) untuk entitas kategori.
        nama_kategori (str): Nama kategori.
        slug_category (str): Slug kategori.
        image_category (str): URL gambar kategori.
        created_at (datetime): Waktu pembuatan kategori.
        updated_at (datetime, opsional): Waktu pembaruan kategori (jika ada).

    Tabel 'category' digunakan untuk menyimpan informasi kategori dalam basis data.
    """

    __tablename__ = "category"

    category_id = Column(Integer, primary_key=True)
    name_category = Column(String)
    slug_category = Column(String)
    image_category = Column(String)

    products = relationship("Product", back_populates="category")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=True)
