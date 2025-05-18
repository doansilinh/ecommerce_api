from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas import ProductBase, ProductCreate, ProductUpdate
from app.crud import products as crud_product
from app.database import get_db

router = APIRouter(tags=["Products"])


@router.get("/", response_model=List[ProductBase], status_code=status.HTTP_200_OK)
def get_all_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_product.get_all_products(db, skip=skip, limit=limit)


@router.get("/{product_id}", response_model=ProductBase, status_code=status.HTTP_200_OK)
def get_product(product_id: str, db: Session = Depends(get_db)):
    product = crud_product.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=ProductBase, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud_product.create_product(db, product)


@router.put("/{product_id}", response_model=ProductBase, status_code=status.HTTP_200_OK)
def update_product(
    product_id: str, product_update: ProductUpdate, db: Session = Depends(get_db)
):
    updated = crud_product.update_product(db, product_id, product_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: str, db: Session = Depends(get_db)):
    deleted = crud_product.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
