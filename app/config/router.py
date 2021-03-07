from fastapi import APIRouter

from app.routers import userRouter

api_router = APIRouter()

api_router.include_router(userRouter.router, prefix="/users")

