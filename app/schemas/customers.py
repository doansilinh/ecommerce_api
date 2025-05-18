from pydantic import BaseModel
from datetime import date


class BaseConfig:
    from_attributes = True


class CustomerBase(BaseModel):
    customer_id: str
    first_name: str
    last_name: str
    gender: str
    birthday: date
    email: str
    phone: str
    marital_status: str
    education: str
    job: str
    nationality: str
    created_at: date
    is_active: str

    class Config(BaseConfig):
        pass


class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    gender: str
    birthday: date
    email: str
    phone: str
    marital_status: str
    education: str
    job: str
    nationality: str

    class Config(BaseConfig):
        pass


class CustomerUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    gender: str | None = None
    birthday: date | None = None
    email: str | None = None
    phone: str | None = None
    marital_status: str | None = None
    education: str | None = None
    job: str | None = None
    nationality: str | None = None
    is_active: str | None = None

    class Config(BaseConfig):
        pass
