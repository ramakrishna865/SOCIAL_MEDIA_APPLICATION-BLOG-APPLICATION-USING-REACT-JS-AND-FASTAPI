# from .database import Base
# from sqlalchemy import Column,Integer,String,ForeignKey
# from sqlalchemy.orm import relationship
# class Blog(Base):
#     __tablename__ = "blogs"
#     id=Column(Integer,primary_key=True,index=True)
#     title=Column(String)
#     body=Column(String)
#     user_id=Column(Integer,ForeignKey('users.id'))

#     creator=relationship("user",back_populates="blogs")


# class user(Base):
#     __tablename__="users"
#     id=Column(Integer,primary_key=True,index=True)
#     name= Column(String)
#     email=Column(String)
#     password=Column(String)

#     blogs=relationship('Blog',back_populates="creator")


# models.py
from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):  # ✅ Use PascalCase for class name
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates="creator")


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")  # ✅ This now matches the class name
