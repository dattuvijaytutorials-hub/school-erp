from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.db.session import engine
from app.db.base import Base
from app.models import user, student
from app.routers import auth

app = FastAPI(title="School ERP")

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="app/templates")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})