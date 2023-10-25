from sqlalchemy import Integer, Column, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base
from .review import Review


class Product(Base):
    __tablename__ = "product"

    product_id = Column(Integer, primary_key=True)
    name = Column(String)
    slug_product = Column(String)
    image_product = Column(String, nullable=True)
    description = Column(String)
    price = Column(Float)
    weight = Column(Float)
    brand = Column(String)
    rating = Column(String)
    count_in_stock = Column(Integer)

    category_id = Column(Integer, ForeignKey("category.category_id"))

    category = relationship("Category", back_populates="products")
    reviews_user = relationship("Review", back_populates="product")

    carts = relationship("Cart", back_populates="product")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=True)
