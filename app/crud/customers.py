from sqlalchemy.orm import Session
from app.models import Customers
from app.schemas import CustomerCreate, CustomerUpdate
import uuid
from datetime import date


def get_all_customer(db: Session, page: int = 0, limit: int = 100):
    return db.query(Customers).offset((page - 1) * limit).limit(limit).all()


def get_customer(db: Session, customer_id: str):
    return db.query(Customers).filter(Customers.customer_id == customer_id).first()


def create_customer(db: Session, customer: CustomerCreate):
    db_customer = Customers(
        customer_id=str(uuid.uuid4()),
        created_at=date.today(),  # sinh ngày hiện tại nếu không có
        is_active="1",  # hoặc giá trị mặc định bạn muốn
        **customer.dict(),
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def update_customer(db: Session, customer_id: str, customer_update: CustomerUpdate):
    db_customer = get_customer(db, customer_id)
    if not db_customer:
        return None
    for key, value in customer_update.dict(exclude_unset=True).items():
        setattr(db_customer, key, value)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def delete_customer(db: Session, customer_id: str):
    db_customer = get_customer(db, customer_id)
    if not db_customer:
        return None
    db.delete(db_customer)
    db.commit()
    return db_customer
