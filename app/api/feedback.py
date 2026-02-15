from fastapi import APIRouter, Depends, Request, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import Optional

from app.db.session import get_db
from app.db.models import Feedback
from app.services.s3_service import upload_file_to_s3

router = APIRouter()


@router.post("/submit-feedback")
def submit_feedback(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    rating: int = Form(...),
    description: Optional[str] = Form(None),
    screenshot: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
):
    client_ip = request.client.host

    screenshot_url = None

    if screenshot:
        screenshot_url = upload_file_to_s3(screenshot)

    new_feedback = Feedback(
        name=name,
        email=email,
        rating=rating,
        description=description,
        screenshot_url=screenshot_url,
        client_ip=client_ip,
    )

    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    return {
        "message": "Feedback submitted successfully",
        "id": new_feedback.id,
        "screenshot_url": screenshot_url,
    }
