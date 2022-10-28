from pydantic import BaseModel

class ProductCreate(BaseModel):
    product_name: str 
    price: str

class ProductUpdate(BaseModel):
    product_name: str 
    price: str

class Product(BaseModel):
    product_id: int
    product_name: str
    price: str
    
    class Config:
        orm_mode = True
