from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

from api.db.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(String(100), nullable=False)
    password = Column(String(1024), nullable=False)
    detail = relationship("UserDetail", back_populates="user")
    token = relationship("UserToken", back_populates="user")


class UserDetail(Base):
    __tablename__ = "user_details"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    email = Column(String(100), nullable=False)
    user = relationship("User", back_populates="user_detail")


class UserToken(Base):
    __tablename__ = "user_token"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    refresh_token = Column(String(1024))
    create_time = DateTime
    user = relationship("User", back_populates="user_token")
