import uuid
from sqlalchemy import Column, String
from app.database import Base


class Suppliers(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(
        String(50), primary_key=True, index=True, default=lambda: str(uuid.uuid4())
    )
    supplier_name = Column(String(50), nullable=False)
    supplier_type = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
