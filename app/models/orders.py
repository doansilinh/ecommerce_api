from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Orders(Base):
    __tablename__ = "oders"

    sale_id = Column(String(50), primary_key=True, index=True)
    product_id = Column(String(50), ForeignKey("products.product_id"))
    customer_id = Column(String(50), ForeignKey("customers.customer_id"))
    employee_id = Column(String(50), ForeignKey("employees.employee_id"))
    date = Column(String(50))
    payment = Column(Integer)
    status = Column(Integer)
    quantity = Column(Integer)

    product = relationship("Products")
    customer = relationship("Customers")
    employee = relationship("Employees")
