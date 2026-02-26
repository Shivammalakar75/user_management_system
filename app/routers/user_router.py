from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.user_service import UserService,UserUpdate
from app.schemas.user_schema import UserCreate, UserResponse,UserRoleUpdate
from app.core.dependencies import get_current_user
from app.db.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

# Register new user
@router.post("/register", response_model=UserResponse)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        return UserService.register_user(db, user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Login user → JWT
from fastapi.security import OAuth2PasswordRequestForm
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    result = UserService.login_user(db, form_data.username, form_data.password)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result

# Get own profile
@router.get("/me", response_model=UserResponse)
def get_me(current_user = Depends(get_current_user)):
    return current_user

# Update own profile
@router.patch("/me", response_model=UserResponse)
def update_me(update_data: UserUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return UserService.update_user(db, current_user.id, update_data, current_user)

# Delete own profile
@router.delete("/me")
def delete_me(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return UserService.delete_user(db, current_user.id, current_user)

# Admin-only: Get all users
@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        return UserService.get_all_users(db, current_user)
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))

@router.patch("/{user_id}/role", response_model=UserResponse)
def admin_update_user_role(
    user_id: int,
    update_data: UserRoleUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return UserService.update_user_role(db, user_id, update_data.role_id, current_user)

# Admin-only: Delete any user
@router.delete("/{user_id}")
def admin_delete_user(user_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        return UserService.delete_user(db, user_id, current_user)
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))