from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.role_service import RoleService
from app.schemas.role_schema import RoleCreate, RoleResponse
from app.core.dependencies import get_current_user
from app.db.database import get_db

router = APIRouter(prefix="/roles", tags=["Roles"])

# Admin-only: Create role
@router.post("/", response_model=RoleResponse)
def create_role(role_data: RoleCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        return RoleService.create_role(db, role_data.name, role_data.description, current_user)
    except (ValueError, PermissionError) as e:
        raise HTTPException(status_code=400 if isinstance(e, ValueError) else 403, detail=str(e))

# Admin-only: Update role
@router.patch("/{role_id}", response_model=RoleResponse)
def update_role(role_id: int, update_data: dict, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        return RoleService.update_role(db, role_id, update_data, current_user)
    except (ValueError, PermissionError) as e:
        raise HTTPException(status_code=400 if isinstance(e, ValueError) else 403, detail=str(e))

# Admin-only: Delete role
@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        return RoleService.delete_role(db, role_id, current_user)
    except (ValueError, PermissionError) as e:
        raise HTTPException(status_code=400 if isinstance(e, ValueError) else 403, detail=str(e))

# Admin-only: Get all roles
@router.get("/", response_model=list[RoleResponse])
def get_all_roles(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        return RoleService.get_all_roles(db, current_user)
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))