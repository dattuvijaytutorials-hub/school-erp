from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.models import user, student  # IMPORTANT: import models

app = FastAPI(title="School ERP")

# Create tables on startup
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "School ERP Running on Render 🚀"}