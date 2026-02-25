from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from .role_schema import RoleResponse


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool
    created_at: datetime
    role: RoleResponse

    model_config = ConfigDict(from_attributes=True)