from typing import Optional
from pydantic import BaseModel, EmailStr
from enum import Enum

class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: Role = Role.USER

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None

class User(UserBase):
    id: str

    class Config:
        orm_mode = True
