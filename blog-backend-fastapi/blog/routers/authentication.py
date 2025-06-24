from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database,models,token
from sqlalchemy.orm import Session
from .. hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
router= APIRouter(
    tags=['authentication']
)
@router.post('/login')
# request:schemas.Login
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"invalid credentials")
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"incorrect password")
    #geneartea jwt token and return 


    
    access_token = token.create_access_token( data={"sub": user.email}
    )
    return {"access_token":access_token, "token_type":"bearer","user_id": user.id ,"user_id": user.id}

    return user



# @router.post('/login')
# def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.email == request.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
#     if not Hash.verify(request.password, user.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")

#     access_token = token.create_access_token(data={"sub": user.email})

#     # 👇 Return explicit JSON response
#     return JSONResponse(content={
#         "access_token": access_token,
#         "token_type": "bearer",
#           # Ensure this is not None
#     })
