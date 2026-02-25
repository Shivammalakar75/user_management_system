from fastapi import FastAPI
from app.routers import user_router, role_router

app = FastAPI(title="User Management System")

# Include routers
app.include_router(user_router.router)
app.include_router(role_router.router)