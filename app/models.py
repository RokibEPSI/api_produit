from sqlalchemy import Column, Integer, String, Text
from .database import Base
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    price = Column(String)
    description = Column(Text)
    color = Column(String)
    stock = Column(String)
    order_id = Column(Integer)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
