from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.coupon_type import CouponType
from app.schemas.coupon_type import CouponTypeSchema

router = APIRouter(
    prefix="/coupon-types",
    tags=["Coupon types"]
)

@router.get("/", response_model=List[CouponTypeSchema])
def get_all(db: Session = Depends(get_db)):
    return db.query(CouponType).all()

@router.get("/{id}", response_model=CouponTypeSchema)
def get_by_id(id: int, db: Session = Depends(get_db)):
    coupon_type = db.query(CouponType).filter(CouponType.id == id).first()
    if not coupon_type:
        raise HTTPException(status_code=404, detail="Tipo de cupon no encontrado")
    return coupon_type