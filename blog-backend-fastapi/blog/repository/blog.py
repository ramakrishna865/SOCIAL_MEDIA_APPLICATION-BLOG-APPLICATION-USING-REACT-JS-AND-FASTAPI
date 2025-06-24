from sqlalchemy.orm import Session
from .. import models,schemas,database,oauth2
from fastapi import HTTPException,status,Depends
def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

# def create(request:schemas.Blog,db:Session):
#     new_blog=models.Blog(title=request.title,body=request.body,user_id=request.id)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog



def create(
    request: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        user_id=current_user.id 
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return {'done'}

def update(id:int,request:schemas.Blog,db:Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    existing_blog = blog_query.first()

    if not existing_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    blog_query.update(request.dict(), synchronize_session=False)
    db.commit()
    return {'detail': 'Blog updated successfully'}

def show(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with the id {id} not available")
        # Response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f"blog with the id {id} not available"}
    return blog