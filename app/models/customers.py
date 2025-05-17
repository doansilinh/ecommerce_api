import uuid
from datetime import date
from sqlalchemy import Column, String, Date
from app.database import Base


class Customers(Base):
    __tablename__ = "customers"

    customer_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String(50))
    last_name = Column(String(50))
    gender = Column(String(10))
    birthday = Column(Date)
    email = Column(String(50))
    phone = Column(String(20))
    marital_status = Column(String(20))
    education = Column(String(20))
    job = Column(String(50))
    nationality = Column(String(50))
    created_at = Column(Date, default=date.today, nullable=False)
    is_active = Column(String, default="1", nullable=False)
