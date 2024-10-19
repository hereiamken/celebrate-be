from pydantic import BaseModel


class UserBase(BaseModel):
    class Config:
        orm_mode = True


class UserCreate(UserBase):
    name: str
    phoneNumber: str
    wish: str
    attend: bool
    cdcr: str

    class Config:
        orm_mode = True
