from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.mall import Mall
from app.schemas.mall import MallSchema, MallCreateSchema, MallUpdateSchema
from typing import List

router = APIRouter(
    prefix="/malls",
    tags=["Malls"]
)

@router.get("/", response_model=List[MallSchema])
def get_all(db: Session = Depends(get_db)):
    return db.query(Mall).all()

@router.get("/{id}", response_model=MallSchema)
def get_by_id(id: int, db: Session = Depends(get_db)):
    mall = db.query(Mall).filter(Mall.id == id).first()
    if not mall:
        raise HTTPException(status_code=404, detail="Mall no encontrado")
    return mall

@router.post("/", response_model=MallSchema)
def create(data: MallCreateSchema, db: Session = Depends(get_db)):
    new_mall = Mall(**data.dict())
    db.add(new_mall)
    db.commit()
    db.refresh(new_mall)
    return new_mall

@router.put("/{id}", response_model=MallSchema)
def update(id: int, data: MallUpdateSchema, db: Session = Depends(get_db)):
    mall = db.query(Mall).filter(Mall.id == id).first()
    if not mall:
        raise HTTPException(status_code=404, detail="Mall no encontrado")

    for campo, valor in data.dict(exclude_unset=True).items():
        setattr(mall, campo, valor)

    db.commit()
    db.refresh(mall)
    return mall

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    mall = db.query(Mall).filter(Mall.id == id).first()
    if not mall:
        raise HTTPException(status_code=404, detail="Mall no encontrado")
    db.delete(mall)
    db.commit()
    return {"ok": True, "mensaje": "Mall eliminado"}