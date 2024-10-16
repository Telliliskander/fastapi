from models.base import Base
from sqlalchemy import Column, Integer

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
