from sqlalchemy.orm import Session
from app.models import Suppliers
from app.schemas import SupplierCreate, SupplierUpdate
import uuid


def get_all_suppliers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Suppliers).offset(skip).limit(limit).all()


def get_supplier(db: Session, supplier_id: str):
    return db.query(Suppliers).filter(Suppliers.supplier_id == supplier_id).first()


def create_supplier(db: Session, supplier: SupplierCreate):
    db_supplier = Suppliers(
        supplier_id=str(uuid.uuid4()),
        **supplier.model_dump(),
    )
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier


def update_supplier(db: Session, supplier_id: str, supplier_update: SupplierUpdate):
    db_supplier = get_supplier(db, supplier_id)
    if not db_supplier:
        return None
    for key, value in supplier_update.model_dump(exclude_unset=True).items():
        setattr(db_supplier, key, value)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier


def delete_supplier(db: Session, supplier_id: str):
    db_supplier = get_supplier(db, supplier_id)
    if not db_supplier:
        return None
    db.delete(db_supplier)
    db.commit()
    return db_supplier
