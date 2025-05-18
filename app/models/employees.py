import uuid
from sqlalchemy import Column, String
from app.database import Base


class Employees(Base):
    __tablename__ = "employees"

    employee_id = Column(
        String(50), primary_key=True, index=True, default=lambda: str(uuid.uuid4())
    )
    employee_name = Column(String(50))
    email = Column(String(50))
    phone = Column(String(20))
    nationality = Column(String(50))
