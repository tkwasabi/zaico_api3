from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from . import models, crud, schemas
from .database import engine, SessionLocal

# Auto creation of database tables

models.Base.metadata.create_all(bind=engine)

# Application bootstrap
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# LIST
@app.get("/read", response_model=List[schemas.Product])
def products_action_list(limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    items = crud.list_products(db, offset, limit)
    return items

# RETRIEVE
@app.get("/read/{product_id}", response_model=schemas.Product)
def products_action_retrieve(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404)
    return product

# CREATE
@app.post("/create", response_model=schemas.ProductCreate)
def product_action_create(data: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = crud.create_product(db, data)
    return product

# UPDATE
@app.put("/update/{product_id}", response_model=schemas.Product)
def products_action_retrieve(product_id: int, data: schemas.ProductUpdate,  db: Session = Depends(get_db)):
    product = crud.update_product(db, product_id, data)
    if product is None:
        raise HTTPException(status_code=404)
    return product


# DELETE
@app.delete("/delete/{product_id}", status_code=204)
def products_action_retrieve(product_id: int,  db: Session = Depends(get_db)):
    crud.delete_product(db, product_id)
    return None