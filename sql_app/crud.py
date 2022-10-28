from sqlalchemy.orm import Session

from .models import Product
from .schemas import ProductCreate, ProductUpdate
from typing import Union

# 製品情報一覧取得
def list_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

# 製品情報取得
def get_product(db: Session, id: int):
    return db.query(Product).get(id)

# 製品情報登録
def create_product(db: Session, data: ProductCreate):
    db_product = Product(**data.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# 製品情報削除
def delete_product(db: Session, product_id: int):
    db.query(Product).filter(Product.product_id == product_id).delete()
    db.commit()
    return None

# 製品情報更新
def update_product(db: Session, product: Union[int, Product], data: ProductUpdate):
    if isinstance(product, int):
        product = get_product(db, product)
    if product is None:
      return None
    for key, value in data:
        setattr(product, key, value)
    db.commit()
    return product