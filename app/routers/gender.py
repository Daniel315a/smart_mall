from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.gender import Gender
from app.schemas.gender import GenderSchema
from typing import List

router=APIRouter(
    prefix="/gender",
    tags=["Gender"]
)

@router.get("/",response_model=list[GenderSchema])
def get_all(db: Session = Depends(get_db)):
    return db.query(Gender).all()


@router.get("/{id}",response_model=GenderSchema)
def get_by_id(id:int,db: Session = Depends(get_db)):
    gender_= db.query(Gender).filter(Gender.id == id).all()
    if not gender_:
        raise HTTPException(status_code=404, detail="genero no encontrado")
    return gender_

