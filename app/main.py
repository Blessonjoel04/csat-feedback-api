from fastapi import FastAPI

# Import database components
from app.db.base import Base
from app.db.session import engine
from app.db import models  # Important: ensures models are registered

# Import routers
from app.api import feedback, admin, report


app = FastAPI(title="CSAT API", version="1.0.0")


# Create tables automatically (only for development)
Base.metadata.create_all(bind=engine)


# Include routers
app.include_router(feedback.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
app.include_router(report.router, prefix="/api")


@app.get("/")
def health_check():
    return {"status": "CSAT API is running - CI/CD pipeline is working!"}
