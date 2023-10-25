from app.database.models.review import Review
from app.database.models.user import User
from app.database.models.product import Product
from .abstract_class.review_abtract import ReviewAbstractRepository
from sqlalchemy.orm import Session
from typing import List
from app.domain.requests.review.create import ReviewRequest


class ReviewRepository(ReviewAbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Review]:
        return self.session.query(Review).all()

    def get_by_id(self, review_id: int) -> Review:
        return self.session.query(Review).filter(Review.id == review_id).first()

    def create_review(
        self, name: str, comment: str, rating: int, user_id: int, product_id: int
    ) -> Review:
        product = self.session.query(Product).filter(Product.product_id == product_id)

        if not product:
            raise

        existing_review = (
            self.session.query(Review)
            .filter(Review.user_id == user_id, Review.product_id == product_id)
            .first()
        )

        if existing_review:
            pass

        review = Review(
            name=name,
            user_id=user_id,
            rating=rating,
            comment=comment,
            product_id=product_id,
        )

        self.session.add(review)
        self.session.commit()
        self.session.refresh(review)

        reviews = (
            self.session.query(Review).filter(Review.product_id == product_id).all()
        )
        total_rating = sum([r.rating for r in reviews])
        total_reviews = len(reviews)

        if total_reviews > 0:
            product.rating = round(total_rating / total_reviews, 2)
        else:
            product.rating = 0.0

        self.session.commit()

        return review
