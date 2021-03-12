from fastapi import APIRouter

from app.routers import users, auth

api_router = APIRouter()

api_router.include_router(users.router, prefix='/users')
api_router.include_router(auth.router, prefix='/auth')