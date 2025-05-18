from sqlalchemy.orm import Session
from app.models import Products
from app.schemas import ProductCreate, ProductUpdate
import uuid


def get_all_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Products).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: str):
    return db.query(Products).filter(Products.product_id == product_id).first()


def create_product(db: Session, product: ProductCreate):
    db_product = Products(
        product_id=str(uuid.uuid4()),
        **product.model_dump(),
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: str, product_update: ProductUpdate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: str):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product
