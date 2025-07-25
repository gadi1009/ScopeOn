
from sqlalchemy.orm import Session
from . import models, schemas

def get_coupon(db: Session, coupon_id: int):
    return db.query(models.Coupon).filter(models.Coupon.id == coupon_id).first()

def get_coupon_by_code(db: Session, code: str):
    return db.query(models.Coupon).filter(models.Coupon.code == code).first()

def get_coupons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Coupon).offset(skip).limit(limit).all()

def create_coupon(db: Session, coupon: schemas.CouponCreate):
    db_coupon = models.Coupon(**coupon.dict())
    db.add(db_coupon)
    db.commit()
    db.refresh(db_coupon)
    return db_coupon

def update_coupon(db: Session, coupon_id: int, coupon: schemas.CouponUpdate):
    db_coupon = db.query(models.Coupon).filter(models.Coupon.id == coupon_id).first()
    if db_coupon:
        for key, value in coupon.dict(exclude_unset=True).items():
            setattr(db_coupon, key, value)
        db.commit()
        db.refresh(db_coupon)
    return db_coupon

def delete_coupon(db: Session, coupon_id: int):
    db_coupon = db.query(models.Coupon).filter(models.Coupon.id == coupon_id).first()
    if db_coupon:
        db.delete(db_coupon)
        db.commit()
    return db_coupon
