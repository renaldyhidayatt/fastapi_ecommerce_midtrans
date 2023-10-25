from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base
from .role import Role
from .cart import Cart


class User(Base):
    """
    Kelas ini mewakili tabel 'user' dalam basis data.

    Atribut:
        user_id (int): Kunci utama (primary key) untuk entitas pengguna.
        firstname (str): Nama depan pengguna.
        lastname (str): Nama belakang pengguna.
        email (str): Alamat email pengguna.
        password (str): Kata sandi pengguna (hash).
        image (str): Nama file gambar profil pengguna (default: "default.jpg").

        role_id (int): Kunci asing (foreign key) menghubungkan pengguna dengan peran (role).
        role (Role): Objek peran (role) terkait dengan pengguna.

        cart_items (list of Cart): Daftar objek keranjang (Cart) terkait dengan pengguna.

        created_at (datetime): Waktu pembuatan akun pengguna.
        updated_at (datetime): Waktu pembaruan akun pengguna (jika ada).

    Tabel 'user' digunakan untuk menyimpan informasi pengguna dalam basis data.
    """

    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    firstname = Column(String(length=30))
    lastname = Column(String(length=30))
    email = Column(String(length=30))
    password = Column(String(length=70))
    image = Column(String, default="default.jpg")

    reviews = relationship("Review", back_populates="user")
    carts = relationship("Cart", back_populates="user")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=True)
