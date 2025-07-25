from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from models import models
from schemas import schemas
from database import SessionLocal, engine

from coupons import router as coupons_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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