from pydantic import BaseModel

class UserReq(BaseModel):
    name: str
    phoneNumber: str = None
    wish: str = None
    attend: bool = False
    cdcr: str

class LoginRequest(BaseModel):
    username: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }