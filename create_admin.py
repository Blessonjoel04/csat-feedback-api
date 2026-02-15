from app.db.session import SessionLocal
from app.db.models import AdminUser
from app.core.security import hash_password

db = SessionLocal()

email = "admin@example.com"
password = "admin123"

existing = db.query(AdminUser).filter(AdminUser.email == email).first()

if not existing:
    new_admin = AdminUser(
        email=email,
        password_hash=hash_password(password),
    )
    db.add(new_admin)
    db.commit()
    print("Admin created successfully!")
else:
    print("Admin already exists.")

db.close()
