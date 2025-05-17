from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas import CustomerBase, CustomerCreate, CustomerUpdate
from app.crud import customers as crud_customer
from app.database import get_db

router = APIRouter(tags=["Customers"])


@router.get("/", response_model=List[CustomerBase], status_code=status.HTTP_200_OK)
def get_all_customers(page: int = 1, limit: int = 100, db: Session = Depends(get_db)):
    """Lấy danh sách khách hàng."""
    return crud_customer.get_all_customer(db, page=page, limit=limit)


@router.get(
    "/{customer_id}", response_model=CustomerBase, status_code=status.HTTP_200_OK
)
def get_customer(customer_id: str, db: Session = Depends(get_db)):
    """Lấy thông tin một khách hàng theo ID."""
    customer = crud_customer.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.post("/", response_model=CustomerBase, status_code=status.HTTP_201_CREATED)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    """Tạo mới một khách hàng."""
    return crud_customer.create_customer(db, customer)


@router.put(
    "/{customer_id}", response_model=CustomerBase, status_code=status.HTTP_200_OK
)
def update_customer(
    customer_id: str, customer_update: CustomerUpdate, db: Session = Depends(get_db)
):
    """Cập nhật thông tin khách hàng."""
    updated = crud_customer.update_customer(db, customer_id, customer_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: str, db: Session = Depends(get_db)):
    """Xóa khách hàng."""
    deleted = crud_customer.delete_customer(db, customer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Customer not found")
