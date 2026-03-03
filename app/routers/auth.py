from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import hash_password
import uuid

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register-parent")
def register_parent(username: str, email: str, password: str, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        username=username,
        email=email,
        password_hash=hash_password(password),
        role="parent"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Parent registered successfully"}