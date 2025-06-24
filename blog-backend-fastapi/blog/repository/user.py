from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status
from .. import hashing
def create(request:schemas.user,db:Session):
    new_user=models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id:int,db:Session):
    user=db.query(models.User).filter(models.User.id==id).filter().first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    return user