
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CouponBase(BaseModel):
    code: str
    discount_type: str
    discount_value: float
    active: Optional[bool] = True
    valid_from: Optional[datetime] = None
    valid_until: Optional[datetime] = None
    minimum_purchase_amount: Optional[float] = 0.0
    usage_limit: Optional[int] = 1

class CouponCreate(CouponBase):
    pass

class CouponUpdate(CouponBase):
    pass

class Coupon(CouponBase):
    id: int
    times_used: int

    class Config:
        orm_mode = True
