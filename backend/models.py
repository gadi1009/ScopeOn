
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from .database import Base
import datetime

class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    discount_type = Column(String)
    discount_value = Column(Float)
    active = Column(Boolean, default=True)
    valid_from = Column(DateTime, default=datetime.datetime.now)
    valid_until = Column(DateTime)
    minimum_purchase_amount = Column(Float, default=0.0)
    usage_limit = Column(Integer, default=1)
    times_used = Column(Integer, default=0)
