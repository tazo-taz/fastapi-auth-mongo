from pydantic import BaseModel, EmailStr
from datetime import datetime, timezone

class UserCreate(BaseModel):
  email: EmailStr
  username: str
  password: str

  class Config:
    json_schema_extra = {
      "example": {
        "email": "samfao.tj@gmail.com",
        "username": "samfao",
        "password": "1111111",
      }
    }
    
class UserLogin(BaseModel):
  email: EmailStr
  password: str

  class Config:
    json_schema_extra = {
      "example": {
        "email": "samfao.tj@gmail.com",
        "password": "1111111",
      }
    }

class User(BaseModel):
  id: str
  email: EmailStr
  username: str
  created_at: datetime = datetime.now(timezone.utc)

  class Config:
    json_schema_extra = {
      "example": {
        "id": "64f1c2a9b7e6d1e3f4a2b123",
        "email": "samfao.tj@gmail.com",
        "username": "samfao",
        "password": "1111111",
        "created_at": "2025-08-31T21:15:00Z",
      }
    }

class Token(BaseModel):
  id: str

  class Config:
    json_schema_extra = {
      "example": {
        "id": "64f1c2a9b7e6d1e3f4a2b123"
      }
    }