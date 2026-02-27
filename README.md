User Management System (FastAPI + JWT) :-
===========================================
A production-ready User Management System built using FastAPI, SQLAlchemy, and JWT Authentication with clean layered architecture.

Features Implemented :-
=========================
Authentication :-
    > User Registration
    > Login with JWT Token
    > Secure Password Hashing
    > OAuth2PasswordBearer integration
    > Protected Routes
    > Self-update only (User cannot update other users)

User Management :-
    > Default role assignment (user)
    > Role-based structure (Admin/User ready)
    > Get Current Logged-in User
    > Update own profile (PATCH /me)
    > Clean Service + Repository architecture

User Capabilities :-
    1. Register account
    2. Login and receive JWT token
    3. Get own profile (GET /me)
    4. Update own profile (PATCH /me)
    5. Cannot update other users
    6. Cannot change own role

Admin Capabilities :-
    Admin role users can:
        1. View all users
        2. Get any user by ID
        3. Update any user
        4. Change user roles
        5. Activate/Deactivate users
        6. Manage role assignments
Admin authorization enforced via role check inside protected routes.

Security :-
    > Password hashing (no plain-text storage)
    > JWT expiry validation
    > Authorization header validation
    > Self-update restriction logic
    > Environment-based secret configuration


Registration Flow :-
======================
1. User sends POST /register
2. Email uniqueness check
3. Password hashing
4. Default role assignment
5. User saved in database
6. User response returned

Login Flow :-
==============
1. User sends POST /login
2. Email verified
3. Password verified
4. JWT token generated
5. Token returned in response

Protected Route Flow :-
========================
1. User sends request with header:
2. Authorization: Bearer <JWT>
3. Token extracted using OAuth2PasswordBearer
4. JWT verified
5. User fetched from database
6. Route executed

Self Update Flow (PATCH /me) :-
================================
1. JWT validated
2. Current user identified
3. Only current_user.id allowed
4. Partial update using exclude_unset
5. Changes committed to database

API Endpoints :-
=================
| Method | Endpoint  | Description        |
| ------ | --------- | ------------------ |
| POST   | /register | Register new user  |
| POST   | /login    | Authenticate user  |
| GET    | /me       | Get current user   |
| PATCH  | /me       | Update own profile |


Technologies Used :-
======================
1. FastAPI
2. SQLAlchemy ORM
3. Pydantic
4. JWT (python-jose or equivalent)
5. MySQL Database

Run the Application :-
=======================
    > uvicorn app.main:app --reload

Open Swagger UI :-
===================
    > http://127.0.0.1:8000/docs

Conclusion :-
===============
This project demonstrates:
    1. Clean layered backend architecture
    2. Secure authentication system
    3. JWT-based authorization
    4. Role-ready user structure
    5. Production-level project organization