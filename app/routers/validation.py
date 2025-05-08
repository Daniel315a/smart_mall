from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.validation import Validation 
from app.schemas.validation import ValidationSchema, ValidationCreateSchema
from typing import List

router=APIRouter(
    prefix="/validation",
    tags=["Validation"]
)

@router.get("/",response_model=List[ValidationSchema])
def get_all(db: Session = Depends(get_db)):
    return db.query(Validation).all()


@router.post("/",response_model=ValidationSchema)
def create_validation(data=ValidationCreateSchema,db: Session = Depends(get_db)):
    new=Validation(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.delete("/{id}",response_model=ValidationSchema)
def delete_validation(id:int,db:Session = Depends(get_db)):
    validation_= db.query(Validation).filter(Validation.id == id).first()
    if not validation_:
        raise HTTPException(status_code=404, detail="validacion no encontrado")
    db.delete(validation_)
    db.commit()
    return {"ok":True, "mensaje":"validacion no encontrada"}