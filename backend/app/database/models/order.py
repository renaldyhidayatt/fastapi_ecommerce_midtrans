from sqlalchemy import Integer, Column, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class Order(Base):
    """
    Kelas ini mewakili tabel 'order' dalam basis data.

    Atribut:
        order_id (str): Kunci utama (primary key) untuk entitas pesanan.
        nama (str): Nama pelanggan yang melakukan pesanan.
        phone (str): Nomor telepon pelanggan.
        provinsi (str): Nama provinsi pengiriman pesanan.
        kota (str): Nama kota pengiriman pesanan.
        alamat (str): Alamat pengiriman pesanan.
        kurir (str): Nama perusahaan kurir pengiriman.
        shipping_method (str): Metode pengiriman pesanan.
        shipping_cost (float): Biaya pengiriman pesanan.
        total_price (float): Total harga pesanan.
        total_product (str): Total produk dalam pesanan.

        user_id (int): Kunci asing (foreign key) yang menghubungkan pesanan dengan pengguna.
        user (User): Objek pengguna terkait dengan pesanan.

        created_at (datetime): Waktu pembuatan pesanan.
        updated_at (datetime, opsional): Waktu pembaruan pesanan (jika ada).

    Tabel 'order' digunakan untuk menyimpan informasi pesanan dalam basis data.
    """

    __tablename__ = "order"

    order_id = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    phone = Column(String(length=100))
    email = Column(String(length=100))

    courier = Column(String(length=100))
    shipping_method = Column(String(length=100))
    shipping_cost = Column(Float)
    total_price = Column(Float)
    total_product = Column(String(length=100))

    transactionId = Column(String(length=255))

    user_id = Column(Integer, ForeignKey("user.user_id"))
    user = relationship("User")

    order_items = relationship("OrderItems", back_populates="order")

    shipping_address = relationship(
        "ShippingAddress", uselist=False, back_populates="order"
    )

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=True)


class ShippingAddress(Base):
    __tablename__ = "shipping"

    id = Column(Integer, primary_key=True, index=True)
    alamat = Column(String)
    provinsi = Column(String)
    negara = Column(String)
    kota = Column(String)
    order_id = Column(Integer, ForeignKey("order.order_id"))

    order = relationship("Order", back_populates="shipping_address")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class OrderItems(Base):
    __tablename__ = "orderitems"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Integer)
    order_id = Column(Integer, ForeignKey("order.order_id"))

    order = relationship("Order", back_populates="order_items")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
