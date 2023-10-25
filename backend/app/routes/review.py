from fastapi import APIRouter, Depends, HTTPException
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.database.models.user import User
from app.service.review_service import ReviewService
from app.domain.requests.review.create import ReviewRequest
from app.repository.review_repository import ReviewRepository
from app.core.token import get_currentUser


reviewrouter = APIRouter(prefix="/review", tags=["Review"])


@reviewrouter.get("/hello")
def hello():
    return "Hello"


@reviewrouter.get("/")
async def get_all(db: Session = Depends(get_db)):
    try:
        review_repository = ReviewRepository(session=db)
        review_service = ReviewService(review_repository=review_repository)

        review = review_service.get_all_reviews()

        return review
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@reviewrouter.get("/{product_id}")
async def get_byid_review(product_id: int, db: Session = Depends(get_db)):
    try:
        review_repository = ReviewRepository(session=db)
        review_service = ReviewService(review_repository=review_repository)

        review = review_service.get_review_by_id(review_id=product_id)

        return review

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@reviewrouter.post("/create/{product_id}")
async def create_review(
    product_id: int,
    request: ReviewRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_currentUser),
):
    try:
        review_repository = ReviewRepository(session=db)
        review_service = ReviewService(review_repository=review_repository)

        review = review_service.create_review(
            product_id=product_id, request=request, current_user=current_user
        )

        return review

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
