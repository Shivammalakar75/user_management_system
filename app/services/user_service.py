from app.core.security import hash_password, verify_password
from app.models.user import User
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate,UserLogin
from app.repositories.user_repository import UserRepository
from app.repositories.role_repository import RoleRepository

class UserService():
    DEFAULT_ROLE_NAME = "user"
    @staticmethod
    def register_user(db: Session, user_data: UserCreate) -> User:
        existing_user = UserRepository.get_user_by_email(db, user_data.email)
        if existing_user:
            raise ValueError("Email already Registered!")
        
        hashed_password = hash_password(user_data.password)
        role = RoleRepository.get_role_by_name(db, UserService.DEFAULT_ROLE_NAME)
        if not role:
            role = RoleRepository.create_role(db, UserService.DEFAULT_ROLE_NAME, "default user role")
        
        user = User(
            name=user_data.name,
            email=user_data.email,
            password=hashed_password,
            role_id=role.id,
            is_active=True
        )
        return UserRepository.create_user(db, user)

    @staticmethod
    def login_user(db: Session, email: str, password: str) -> User | None:
        user = UserRepository.get_user_by_email(db, email)
        if not user:
            return None
        
        if not verify_password(password, user.password):
            return None
        
        return user
    
    @staticmethod
    def get_user(db: Session, user_id: int, current_user: User):
        user = UserRepository.get_user_by_id(db, user_id)

        if not user:
            raise ValueError("user not found!")
        
        if current_user.role.name != "admin" and current_user.id != user.id:
            raise
    

    
