from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.city import City
from app.schemas.city import CitySchema

router = APIRouter(
    prefix="/cities",
    tags=["Cities"]
)

@router.get("/region/{region_id}", response_model=List[CitySchema])
def get_by_region(region_id: int, db: Session = Depends(get_db)):
    return db.query(City).filter(City.region_id == region_id).all()

@router.get("/{id}", response_model=CitySchema)
def get_by_id(id: int, db: Session = Depends(get_db)):
    ciudad = db.query(City).filter(City.id == id).first()
    if not ciudad:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")
    return ciudad