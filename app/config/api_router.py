from fastapi import APIRouter

from app.routers import user_router, auth_router

api_router = APIRouter()

api_router.include_router(user_router.router, prefix='/users')
api_router.include_router(auth_router.router, prefix='/auth')
