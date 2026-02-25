from sqlalchemy import Integer, String, Boolean, TIMESTAMP, ForeignKey,func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class User(Base):
    """This is User ORM model class which is mapped with users table in user_management_DB (mysql)"""
    
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())

    role = relationship("Role", back_populates="users")