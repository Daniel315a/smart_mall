from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserSchema, UserCreateSchema, UserUpdateSchema
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=List[UserSchema])
def get_all(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{id}", response_model=UserSchema)
def get_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.post("/", response_model=UserSchema)
def create(data: UserCreateSchema, db: Session = Depends(get_db)):
    new = User(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.put("/{id}", response_model=UserSchema)
def update(id: int, data: UserUpdateSchema, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    for campo, valor in data.dict(exclude_unset=True).items():
        setattr(usuario, campo, valor)

    db.commit()
    db.refresh(usuario)
    return usuario

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"ok": True, "mensaje": "Usuario eliminado"}
