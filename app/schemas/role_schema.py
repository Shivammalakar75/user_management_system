# app/schemas/role_schema.py

from pydantic import BaseModel,ConfigDict
from datetime import datetime


class RoleBase(BaseModel):
    name: str
    description: str | None = None


class RoleResponse(RoleBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)