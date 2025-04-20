from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_role import UserRole
from app.schemas.user_role import UserRoleSchema
from typing import List
from fastapi import HTTPException

router = APIRouter(
    prefix="/user-roles",
    tags=["User Roles"]
)

@router.get("/", response_model=List[UserRoleSchema])
def get_all(db: Session = Depends(get_db)):
    return db.query(UserRole).all()

@router.get("/{id}", response_model=UserRoleSchema)
def get_by_id(id: int, db: Session = Depends(get_db)):
    rol = db.query(UserRole).filter(UserRole.id == id).first()
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol
