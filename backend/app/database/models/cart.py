from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base
from .product import Product


class Cart(Base):
    __tablename__ = "cart"

    cart_id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    image = Column(String)
    quantity = Column(Integer)
    weight = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    product_id = Column(Integer, ForeignKey("product.product_id"))
    user = relationship("User", back_populates="carts")
    product = relationship("Product", back_populates="carts")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
