# app/services/role_service.py

from sqlalchemy.orm import Session
from app.repositories.role_repository import RoleRepository
from app.repositories.user_repository import UserRepository
from app.models.role import Role
from app.models.user import User

class RoleService:

    @staticmethod
    def create_role(db: Session, name: str, description: str, current_user: User) -> Role:
        if current_user.role.name != "admin":
            raise PermissionError("Access denied")

        existing_role = RoleRepository.get_role_by_name(db, name)
        if existing_role:
            raise ValueError("Role already exists")

        return RoleRepository.create_role(db, name, description)

    @staticmethod
    def update_role(db: Session, role_id: int, update_data: dict, current_user: User) -> Role:
        if current_user.role.name != "admin":
            raise PermissionError("Access denied")

        role = RoleRepository.get_role_by_id(db, role_id)
        if not role:
            raise ValueError("Role not found")

        return RoleRepository.update_role(db, role, update_data)

    @staticmethod
    def delete_role(db: Session, role_id: int, current_user: User):
        if current_user.role.name != "admin":
            raise PermissionError("Access denied")

        role = RoleRepository.get_role_by_id(db, role_id)
        if not role:
            raise ValueError("Role not found")

        linked_users = db.query(User).filter(User.role_id == role.id).all()
        if linked_users:
            raise ValueError("Cannot delete role: linked users exist")

        RoleRepository.delete_role(db, role)
        return {"message": "Role deleted successfully"}

    @staticmethod
    def get_role_by_id(db: Session, role_id: int, current_user: User) -> Role:
        if current_user.role.name != "admin":
            raise PermissionError("Access denied")

        role = RoleRepository.get_role_by_id(db, role_id)
        if not role:
            raise ValueError("Role not found")
        return role

    @staticmethod
    def get_all_roles(db: Session, current_user: User) -> list[Role]:
        if current_user.role.name != "admin":
            raise PermissionError("Access denied")

        return db.query(Role).all()