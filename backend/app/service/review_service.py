from .abstract_class.review_abstract import ReviewAbstractService
from app.repository.abstract_class.review_abtract import ReviewAbstractRepository
from app.domain.requests.review.create import ReviewRequest
from app.database.models.user import User


class ReviewService(ReviewAbstractService):
    def __init__(self, review_repository: ReviewAbstractRepository):
        self.review_repository = review_repository

    def get_all_reviews(self):
        return self.review_repository.get_all()

    def get_review_by_id(self, review_id):
        return self.review_repository.get_by_id(review_id)

    def create_review(
        self, product_id: int, request: ReviewRequest, current_user: User
    ):
        return self.review_repository.create_review(
            name=current_user.firstname + " " + current_user.lastname,
            comment=request.comment,
            rating=request.rating,
            user_id=current_user.user_id,
            product_id=product_id,
        )
