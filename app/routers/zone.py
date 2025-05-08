from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.zone import Zone
from app.schemas.zone import ZoneSchema, ZoneCreateSchema, ZoneUpdateSchema
from typing import List

router = APIRouter(
    prefix="/zones",
    tags=["Zones"]
)

@router.post("/", response_model=ZoneSchema)
def create(data: ZoneCreateSchema, db: Session = Depends(get_db)):
    new_zone = Zone(**data.dict())
    db.add(new_zone)
    db.commit()
    db.refresh(new_zone)
    return new_zone

@router.get("/mall/{mall_id}", response_model=List[ZoneSchema])
def get_all_by_mall(mall_id: int, db: Session = Depends(get_db)):
    return db.query(Zone).filter(Zone.mall_id == mall_id).all()

@router.get("/{id}", response_model=ZoneSchema)
def get_by_id(id: int, db: Session = Depends(get_db)):
    zone = db.query(Zone).filter(Zone.id == id).first()
    if not zone:
        raise HTTPException(status_code=404, detail="Zona no encontrada")
    return zone

@router.put("/{id}", response_model=ZoneSchema)
def update_name(id: int, data: ZoneUpdateSchema, db: Session = Depends(get_db)):
    zone = db.query(Zone).filter(Zone.id == id).first()
    if not zone:
        raise HTTPException(status_code=404, detail="Zona no encontrada")

    if data.name is not None:
        zone.name = data.name

    db.commit()
    db.refresh(zone)
    return zone

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    zone = db.query(Zone).filter(Zone.id == id).first()
    if not zone:
        raise HTTPException(status_code=404, detail="Zona no encontrada")
    db.delete(zone)
    db.commit()
    return {"ok": True, "mensaje": "Zona eliminada"}