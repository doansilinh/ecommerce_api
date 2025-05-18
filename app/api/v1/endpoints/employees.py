from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas import EmployeeBase, EmployeeCreate, EmployeeUpdate
from app.crud import employees as crud_employee
from app.database import get_db

router = APIRouter(tags=["Employees"])


@router.get("/", response_model=List[EmployeeBase], status_code=status.HTTP_200_OK)
def get_all_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_employee.get_all_employees(db, skip=skip, limit=limit)


@router.get(
    "/{employee_id}", response_model=EmployeeBase, status_code=status.HTTP_200_OK
)
def get_employee(employee_id: str, db: Session = Depends(get_db)):
    employee = crud_employee.get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.post("/", response_model=EmployeeBase, status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return crud_employee.create_employee(db, employee)


@router.put(
    "/{employee_id}", response_model=EmployeeBase, status_code=status.HTTP_200_OK
)
def update_employee(
    employee_id: str, employee_update: EmployeeUpdate, db: Session = Depends(get_db)
):
    updated = crud_employee.update_employee(db, employee_id, employee_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated


@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: str, db: Session = Depends(get_db)):
    deleted = crud_employee.delete_employee(db, employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
