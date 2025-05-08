from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.store import Store
from app.schemas.store import StoreSchema, StoreCreateSchema, StoreUpdateSchema

router = APIRouter(
    prefix="/stores",
    tags=["Stores"]
)

@router.post("/", response_model=StoreSchema)
def create(data: StoreCreateSchema, db: Session = Depends(get_db)):
    new_store = Store(**data.dict())
    db.add(new_store)
    db.commit()
    db.refresh(new_store)
    return new_store

@router.get("/mall/{mall_id}", response_model=List[StoreSchema])
def get_by_mall(mall_id: int, db: Session = Depends(get_db)):
    return db.query(Store).join(Store.zone).filter(Store.zone.has(mall_id=mall_id)).all()

@router.get("/zone/{zone_id}", response_model=List[StoreSchema])
def get_by_zone(zone_id: int, db: Session = Depends(get_db)):
    return db.query(Store).filter(Store.zone_id == zone_id).all()

@router.get("/{id}", response_model=StoreSchema)
def get_by_id(id: int, db: Session = Depends(get_db)):
    store = db.query(Store).filter(Store.id == id).first()
    if not store:
        raise HTTPException(status_code=404, detail="Tienda no encontrada")
    return store

@router.put("/{id}", response_model=StoreSchema)
def update(id: int, data: StoreUpdateSchema, db: Session = Depends(get_db)):
    store = db.query(Store).filter(Store.id == id).first()
    if not store:
        raise HTTPException(status_code=404, detail="Tienda no encontrada")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(store, field, value)

    db.commit()
    db.refresh(store)
    return store

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    store = db.query(Store).filter(Store.id == id).first()
    if not store:
        raise HTTPException(status_code=404, detail="Tienda no encontrada")
    db.delete(store)
    db.commit()
    return {"ok": True, "mensaje": "Tienda eliminada"}