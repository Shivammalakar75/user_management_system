
# app/repositories/role_repository.py

from sqlalchemy.orm import Session
from app.models.role import Role

class RoleRepository:
    @staticmethod
    def get_role_by_name(db: Session, name: str) -> Role | None:
        return db.query(Role).filter(Role.name == name).first()

    @staticmethod
    def get_role_by_id(db: Session, role_id: int) -> Role | None:
        return db.query(Role).filter(Role.id == role_id).first()

    @staticmethod
    def create_role(db: Session, name: str, description: str | None = None) -> Role:
        role = Role(name=name, description=description)
        db.add(role)
        db.commit()
        db.refresh(role)
        return role
    
    @staticmethod
    def update_role(db: Session, role: Role, update_data: dict) -> Role:
        """
        role: ORM Role object
        update_data: dictionary with fields to update (name, description)
        """
        for key, value in update_data.items():
            setattr(role, key, value)
        db.commit()
        db.refresh(role)
        return role
    
    @staticmethod
    def delete_role(db: Session, role: Role):
        db.delete(role)
        db.commit()