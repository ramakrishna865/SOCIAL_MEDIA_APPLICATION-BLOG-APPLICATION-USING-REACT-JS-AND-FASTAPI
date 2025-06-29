from fastapi import APIRouter,Depends,status,HTTPException

from .. import schemas ,database,models,oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

from ..repository import blog
router=APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

@router.get('/',response_model=list[schemas.showBlog])
def all(db:Session = Depends(database.get_db),current_user:schemas.user=Depends(oauth2.get_current_user)):
    return blog.get_all(db)
    


@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(database.get_db),current_user:schemas.user=Depends(oauth2.get_current_user)):
    return blog.create(request,db)


@router.get('/{id}',response_model=schemas.showBlog,status_code=200)
def show(id,db:Session = Depends(database.get_db),current_user:schemas.user=Depends(oauth2.get_current_user)):
    return blog.show(id,db);

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(database.get_db),current_user:schemas.user=Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db),current_user:schemas.user=Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)