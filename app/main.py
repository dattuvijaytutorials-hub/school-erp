from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.models import user, student
from app.routers import auth

app = FastAPI(title="School ERP")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def home():
    return {"message": "School ERP Running on Render 🚀"}