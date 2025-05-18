from pydantic import BaseModel


class BaseConfig:
    from_attributes = True


class EmployeeBase(BaseModel):
    employee_id: str
    employee_name: str
    email: str
    phone: str
    nationality: str

    class Config(BaseConfig):
        pass


class EmployeeCreate(BaseModel):
    employee_name: str
    email: str
    phone: str
    nationality: str

    class Config(BaseConfig):
        pass


class EmployeeUpdate(BaseModel):
    employee_name: str | None = None
    email: str | None = None
    phone: str | None = None
    nationality: str | None = None

    class Config(BaseConfig):
        pass
