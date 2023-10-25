from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from app.core.database import Base
from datetime import datetime


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    comment = Column(String(255))
    rating = Column(Integer)

    user_id = Column(Integer, ForeignKey("user.user_id"))
    user = relationship("User", back_populates="reviews")

    product_id = Column(Integer, ForeignKey("product.product_id"))
    product = relationship("Product", back_populates="reviews_user")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
