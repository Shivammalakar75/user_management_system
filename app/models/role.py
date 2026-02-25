from sqlalchemy import Integer, String, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Role(Base):
    """this is Role ORM model class which is mapped with roles table in user_management_DB (mysql)"""
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[String] = mapped_column(String(20), unique=True, nullable=False)
    description: Mapped[String] = mapped_column(String(255), nullable=True)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())
    
    #relationship (One role ---> Many users)
    users = relationship("User", back_populates="role")
