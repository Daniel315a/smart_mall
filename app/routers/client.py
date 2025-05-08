from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.client import Client 
from app.schemas.client import ClientSchema, ClientCreateSchema , ClientUpdateSchema
from typing import List
from app.models.validation import Validation

router=APIRouter(
    prefix="/client",
    tags=["Client"]
)

@router.get("/", response_model=List[ClientSchema])
def get_all(db: Session = Depends(get_db)):
    return db.query(Client).all()

@router.get("/{id}",response_model=List[ClientSchema])
def get_client_validation(id:int,db: Session = Depends(get_db)):
    result= db.query(Validation).join(Client.id).all()
    return result 



@router.post("/",response_model=ClientSchema)
def create_client(data:ClientCreateSchema,db: Session = Depends(get_db)):
    new=Client(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.put("/{id}",response_model=ClientUpdateSchema)
def update(id:int,data:ClientUpdateSchema,db: Session = Depends(get_db)):
    client_=db.query(Client).filter(Client.id==id).first()
    if not client_:
        raise HTTPException(status_code=404,detail="cliente no encontrado")
    
    for campo,valor in data.dict(exclude_unset=True).items():
        setattr(client_,campo,valor)
    
    db.commit()
    db.refresh(client_)
    return client_

@router.delete("/{id}")
def delete_client(id:int, db: Session = Depends(get_db)):
    client_=db.query(Client).filter(Client.id==id).firts()
    if not client_:
        raise HTTPException(status_code=404,detail="cliente no encontrado")
    db.delete(client_)
    db.commit()
    return {"ok":True,"mensaje":"U¿Cliente eliminado"}