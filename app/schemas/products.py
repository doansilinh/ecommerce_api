from pydantic import BaseModel


class BaseConfig:
    from_attributes = True


class ProductBase(BaseModel):
    product_id: str
    product_name: str
    category: str
    supplier_id: str
    price: float
    discount: float

    class Config(BaseConfig):
        pass


class ProductCreate(BaseModel):
    product_name: str
    category: str
    supplier_id: str
    price: float
    discount: float

    class Config(BaseConfig):
        pass


class ProductUpdate(BaseModel):
    product_name: str | None = None
    category: str | None = None
    supplier_id: str | None = None
    price: float | None = None
    discount: float | None = None

    class Config(BaseConfig):
        pass
