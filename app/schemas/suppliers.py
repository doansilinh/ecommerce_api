from pydantic import BaseModel


class BaseConfig:
    from_attributes = True


class SupplierBase(BaseModel):
    supplier_id: str
    supplier_name: str
    supplier_type: str
    country: str
    email: str
    phone: str

    class Config(BaseConfig):
        pass


class SupplierCreate(BaseModel):
    supplier_name: str
    supplier_type: str
    country: str
    email: str
    phone: str

    class Config(BaseConfig):
        pass


class SupplierUpdate(BaseModel):
    supplier_name: str | None = None
    supplier_type: str | None = None
    country: str | None = None
    email: str | None = None
    phone: str | None = None

    class Config(BaseConfig):
        pass
