from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from app.core.database import get_db
from app.database.models.user import User
from app.database.models.product import Product
from app.database.models.order import Order


dashboardrouter = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@dashboardrouter.get("/dashboard")
def get_dashboard(db: Session = Depends(get_db)):
    try:
        db = next(get_db())
        user_count = db.query(User).count()
        product_count = db.query(Product).count()
        order_count = db.query(Order).count()

        yearly_revenue = calculate_yearly_revenue(db)

        total_revenue = db.query(func.sum(Order.total_price)).scalar() or 0

        return {
            "user": user_count,
            "product": product_count,
            "order": order_count,
            "pendapatan": yearly_revenue,
            "totalPendapatan": total_revenue,
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def calculate_yearly_revenue(db):
    yearly_revenue = []
    for month in range(1, 13):
        total_revenue = (
            db.query(func.sum(Order.total_price))
            .filter(func.extract("month", Order.created_at) == month)
            .scalar()
            or 0
        )
        yearly_revenue.append(total_revenue)
    return yearly_revenue
