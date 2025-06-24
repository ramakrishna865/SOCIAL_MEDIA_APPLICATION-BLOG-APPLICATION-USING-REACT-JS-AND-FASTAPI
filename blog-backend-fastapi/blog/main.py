from fastapi import FastAPI
from .database import engine
from .routers import blog,user,authentication
from . import schemas,models
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


























# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/blog",status_code=status.HTTP_201_CREATED,tags=['blogs'])
# def create(request:schemas.Blog,db:Session=Depends(get_db)):
#     new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.get('/blog',response_model=list[schemas.showBlog],tags=['blogs'])
# def all(db:Session = Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}',response_model=schemas.showBlog,status_code=200,tags=['blogs'])
# def show(id,db:Session = Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with the id {id} not available")
#         # Response.status_code=status.HTTP_404_NOT_FOUND
#         # return {'detail':f"blog with the id {id} not available"}
#     return blog

# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
# def destroy(id,db:Session = Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
#     db.commit()
#     return {'done'}

# @app.put("/blog/{id}",status_code=status.HTTP_201_CREATED)
# def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id).update(request)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
    
#     db.commit()
#     return 'updated'

# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
# def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog_query = db.query(models.Blog).filter(models.Blog.id == id)
#     existing_blog = blog_query.first()

#     if not existing_blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

#     blog_query.update(request.dict(), synchronize_session=False)
#     db.commit()
#     return {'detail': 'Blog updated successfully'}



# @app.post('/user',response_model=schemas.showUser,tags=['users'])
# def create_user(request:schemas.user,db: Session = Depends(get_db)):
    
#     new_user=models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get('/user/{id}',response_model=schemas.showUser,tags=['users'])
# def get_user(id:int,db: Session = Depends(get_db)):
#     user=db.query(models.User).filter(models.User.id==id).filter().first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
#     return user

