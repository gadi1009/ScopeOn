
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/coupons",
    tags=["coupons"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Coupon)
def create_coupon(coupon: schemas.CouponCreate, db: Session = Depends(get_db)):
    db_coupon = crud.get_coupon_by_code(db, code=coupon.code)
    if db_coupon:
        raise HTTPException(status_code=400, detail="Coupon code already registered")
    return crud.create_coupon(db=db, coupon=coupon)

@router.get("/", response_model=List[schemas.Coupon])
def read_coupons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    coupons = crud.get_coupons(db, skip=skip, limit=limit)
    return coupons

@router.get("/{coupon_id}", response_model=schemas.Coupon)
def read_coupon(coupon_id: int, db: Session = Depends(get_db)):
    db_coupon = crud.get_coupon(db, coupon_id=coupon_id)
    if db_coupon is None:
        raise HTTPException(status_code=404, detail="Coupon not found")
    return db_coupon

@router.put("/{coupon_id}", response_model=schemas.Coupon)
def update_coupon(coupon_id: int, coupon: schemas.CouponUpdate, db: Session = Depends(get_db)):
    db_coupon = crud.update_coupon(db, coupon_id=coupon_id, coupon=coupon)
    if db_coupon is None:
        raise HTTPException(status_code=404, detail="Coupon not found")
    return db_coupon

@router.delete("/delete/{coupon_id}", response_model=schemas.Coupon)
def delete_coupon(coupon_id: int, db: Session = Depends(get_db)):
    db_coupon = crud.delete_coupon(db, coupon_id=coupon_id)
    if db_coupon is None:
        raise HTTPException(status_code=404, detail="Coupon not found")
    return db_coupon
