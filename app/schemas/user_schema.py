from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from .role_schema import RoleResponse
from typing import Optional
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

class UserRoleUpdate(BaseModel):
    role_id: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None