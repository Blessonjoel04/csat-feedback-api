from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta

from app.db.session import get_db
from app.db.models import Feedback
from app.core.security import get_current_user

router = APIRouter()


@router.get("/report/summary")
def get_report(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    now = datetime.utcnow()

    total_avg = db.query(func.avg(Feedback.rating)).scalar()

    avg_30 = db.query(func.avg(Feedback.rating)).filter(
        Feedback.created_at >= now - timedelta(days=30)
    ).scalar()

    avg_60 = db.query(func.avg(Feedback.rating)).filter(
        Feedback.created_at >= now - timedelta(days=60)
    ).scalar()

    avg_90 = db.query(func.avg(Feedback.rating)).filter(
        Feedback.created_at >= now - timedelta(days=90)
    ).scalar()

    unique_ratings = db.query(func.count(func.distinct(Feedback.rating))).scalar()

    return {
        "total_average_rating": round(total_avg, 2) if total_avg else 0,
        "average_last_30_days": round(avg_30, 2) if avg_30 else 0,
        "average_last_60_days": round(avg_60, 2) if avg_60 else 0,
        "average_last_90_days": round(avg_90, 2) if avg_90 else 0,
        "unique_ratings_count": unique_ratings or 0,
    }
