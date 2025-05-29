import os
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserSchema, UserCreateSchema, UserWithTokenSchema
from typing import List
from jose import jwt
from dotenv import load_dotenv
from app.models.mall import Mall

load_dotenv()

jwt_secret = os.getenv("SECRET_KEY")
jwt_algorithm = os.getenv("JWT_ALGORITHM")

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

@router.post("/sync", response_model=UserWithTokenSchema)
def sync_user(data: UserCreateSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if user:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(user, key, value)
    else:
        mall = db.query(Mall).first()

        if not mall:
            raise HTTPException(status_code=400, detail="No hay 'malls' en la base de datos")
        
        user = User(**data.dict(), mall_id=mall.id)
        db.add(user)

    db.commit()
    db.refresh(user)

    payload = {
        "sub": user.auth0_id,
        "role_id": user.role_id
    }

    token = jwt.encode(payload, jwt_secret, algorithm=jwt_algorithm)

    return {
        "user": UserSchema.model_validate(user),
        "token": token
    }

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"ok": True, "mensaje": "Usuario eliminado"}
