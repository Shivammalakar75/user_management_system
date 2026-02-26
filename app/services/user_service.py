# app/services/user_service.py

from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.repositories.role_repository import RoleRepository
from app.models.user import User
from app.core.security import hash_password, verify_password
from app.schemas.user_schema import UserCreate
from app.core.security import create_access_token
from datetime import timedelta
# from fastapi import Depends
# from db.database import get_db

class UserService:
    DEFAULT_ROLE_NAME = "user"  

    @staticmethod
    def register_user(db: Session, user_data: UserCreate) -> User:
        existing_user = UserRepository.get_user_by_email(db, user_data.email)
        if existing_user:
            raise ValueError("Email already registered")

        hashed_password = hash_password(user_data.password)

        role = RoleRepository.get_role_by_name(db, UserService.DEFAULT_ROLE_NAME)
        if not role:
            role = RoleRepository.create_role(db, UserService.DEFAULT_ROLE_NAME, "Default user role")

        user = User(
            name=user_data.name,
            email=user_data.email,
            password=hashed_password,
            role_id=role.id,
            is_active=True
        )

        return UserRepository.create_user(db, user)

    @staticmethod
    def login_user(db: Session, email: str, password: str) -> dict | None:
        user = UserRepository.get_user_by_email(db, email)
        if not user or not verify_password(password, user.password):
            return None

        # JWT token create
        access_token_expires = timedelta(minutes=60)
        token = create_access_token(
            data={"user_id": user.id, "role": user.role.name},
            expires_delta=access_token_expires
        )
        return {"access_token": token, "token_type": "bearer", "user": user}

    @staticmethod
    def get_user(db: Session, user_id: int, current_user: User) -> User:
        user = UserRepository.get_user_by_id(db, user_id)
        if not user:
            raise ValueError("User not found")

        if current_user.role.name != "admin" and current_user.id != user.id:
            raise PermissionError("Access denied")

        return user

    @staticmethod
    def get_all_users(db: Session, current_user: User) -> list[User]:
        if current_user.role.name != "admin":
            raise PermissionError("Access denied")
        return UserRepository.get_all_users(db)

    # @staticmethod
    # def update_user(db: Session, user_id: int, update_data: dict, current_user: User) -> User:
    #     user = UserRepository.get_user_by_id(db, user_id)
    #     if not user:
    #         raise ValueError("User not found")

    #     if current_user.role.name != "admin" and current_user.id != user.id:
    #         raise PermissionError("Access denied")

    #     # Not Complete Logic
    #     if "password" in update_data:
    #         update_data["password"] = hash_password(update_data["password"])

    #     return UserRepository.update_user(db, user, update_data)

    @staticmethod
    def delete_user(db: Session, user_id: int, current_user: User):
        user = UserRepository.get_user_by_id(db, user_id)
        if not user:
            raise ValueError("User not found")

        if current_user.role.name != "admin" and current_user.id != user.id:
            raise PermissionError("Access denied")

        UserRepository.delete_user(db, user)
        return {"message": "User deleted successfully"}