from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas import SupplierBase, SupplierCreate, SupplierUpdate
from app.crud import suppliers as crud_supplier
from app.database import get_db

router = APIRouter(tags=["Suppliers"])


@router.get("/", response_model=List[SupplierBase], status_code=status.HTTP_200_OK)
def get_all_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_supplier.get_all_suppliers(db, skip=skip, limit=limit)


@router.get(
    "/{supplier_id}", response_model=SupplierBase, status_code=status.HTTP_200_OK
)
def get_supplier(supplier_id: str, db: Session = Depends(get_db)):
    supplier = crud_supplier.get_supplier(db, supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier


@router.post("/", response_model=SupplierBase, status_code=status.HTTP_201_CREATED)
def create_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    return crud_supplier.create_supplier(db, supplier)


@router.put(
    "/{supplier_id}", response_model=SupplierBase, status_code=status.HTTP_200_OK
)
def update_supplier(
    supplier_id: str, supplier_update: SupplierUpdate, db: Session = Depends(get_db)
):
    updated = crud_supplier.update_supplier(db, supplier_id, supplier_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return updated


@router.delete("/{supplier_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supplier(supplier_id: str, db: Session = Depends(get_db)):
    deleted = crud_supplier.delete_supplier(db, supplier_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Supplier not found")
