from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from models import models
from schemas import schemas
from database import SessionLocal, engine

from coupons import router as coupons_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="backend/templates")

app.include_router(coupons_router.router)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Coupon Management API!"}

@app.get("/coupons/", response_model=List[schemas.Coupon])
def read_coupons(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    coupons = crud.get_coupons(db, skip=skip, limit=limit)
    if "HX-Request" in request.headers:
        return templates.TemplateResponse("coupon_list_partial.html", {"request": request, "coupons": coupons})
    return coupons