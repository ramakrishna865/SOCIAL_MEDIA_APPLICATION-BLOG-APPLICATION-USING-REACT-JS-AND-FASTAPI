from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from .. import database,schemas,models
from ..hashing import Hash
from ..repository import user
router=APIRouter(
    prefix="/user",
    tags=["users"]
)

get_db=database.get_db


@router.post('/',response_model=schemas.showUser,tags=['users'])
def create_user(request:schemas.user,db: Session = Depends(get_db)):
    return user.create(request,db)


@router.get('/{id}',response_model=schemas.showUser,tags=['users'])
def get_user(id:int,db: Session = Depends(get_db)):
    return user.get(id,db)
    

