from sqlalchemy import Column, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.database import Base


class Products(Base):
    __tablename__ = "products"

    product_id = Column(String(50), primary_key=True, index=True)
    product_name = Column(String(50))
    category = Column(String(50))
    supplier_id = Column(String(50), ForeignKey("suppliers.supplier_id"))
    price = Column(Numeric(10, 2))
    discount = Column(Numeric(5, 2))

    supplier = relationship("Suppliers")
