from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.region import Region
from app.schemas.region import RegionSchema

router = APIRouter(
    prefix="/regions",
    tags=["Regions"]
)

@router.get("/", response_model=List[RegionSchema])
def get_all(db: Session = Depends(get_db)):
    return db.query(Region).all()

@router.get("/{id}", response_model=RegionSchema)
def get_by_id(id: int, db: Session = Depends(get_db)):
    region = db.query(Region).filter(Region.id == id).first()
    if not region:
        raise HTTPException(status_code=404, detail="Región no encontrada")
    return region