from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.coupon import Coupon 
from app.schemas.coupon import CouponSchema , CuponCreateSchema
from typing import List

from app.models.store import Store


router = APIRouter(
    prefix="/coupon",
    tags=["Coupon"]
)

@router.get("/",response_model=List[CouponSchema])
def get_all(db:Session=Depends(get_db)):
    return db.query(Coupon).all()

@router.get("/{store_id}",response_model=CouponSchema)
def get_by_store_id(store_id:int, db:Session=Depends(get_db)):
    coupon=db.query(Coupon).filter(Coupon.store_id==store_id).all()
    if not coupon:
        raise HTTPException(status_code=404,detail="Cupon no encontrado")
    return coupon

@router.get("/{store_id}",response_model=CouponSchema)
def get_coupon_store(store_id:int,db:Session=Depends(get_db)):
    result = db.query(Store).join(Coupon.store_id).all()
    return result 

@router.post("/",response_model=CouponSchema)
def create(data:CuponCreateSchema,db: Session = Depends(get_db)):
    new=Coupon(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.delete("/{id}")
def delete_coupon(id:int, db: Session = Depends(get_db)):
    coupon=db.query(Coupon).filter(Coupon.id==id).first()
    if not coupon:
        raise HTTPException(status_code=404,detail="coupon no encontrado")
    db.delete(coupon)
    db.commit()
    return {"ok":True,"mensaje":"Cupon eliminado"}




