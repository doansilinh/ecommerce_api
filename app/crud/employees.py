from sqlalchemy.orm import Session
from app.models import Employees
from app.schemas import EmployeeCreate, EmployeeUpdate
import uuid


def get_all_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Employees).offset(skip).limit(limit).all()


def get_employee(db: Session, employee_id: str):
    return db.query(Employees).filter(Employees.employee_id == employee_id).first()


def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employees(
        employee_id=str(uuid.uuid4()),
        **employee.model_dump(),
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(db: Session, employee_id: str, employee_update: EmployeeUpdate):
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return None
    for key, value in employee_update.model_dump(exclude_unset=True).items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, employee_id: str):
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return None
    db.delete(db_employee)
    db.commit()
    return db_employee
