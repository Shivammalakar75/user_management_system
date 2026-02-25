from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> User | None:
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_all_users(db: Session) -> list[User]:
        return db.query(User).all()

    @staticmethod
    def create_user(db: Session, user: User) -> User:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def update_user(db: Session, user: User, update_data: dict) -> User:
        """
        user: ORM User object (already fetched from DB)
        update_data: dictionary with fields to update
        """
        for key, value in update_data.items():
            setattr(user, key, value)  
        db.commit()   
        db.refresh(user)  
        return user

    @staticmethod
    def delete_user(db: Session, user: User):
        db.delete(user)
        db.commit()