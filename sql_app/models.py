from sqlalchemy import Column, Integer, String

from .database import Base

class Product(Base):
    __tablename__ = 'products'
    
    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, unique=True, index=True)
    price = Column(Integer, index=True)
