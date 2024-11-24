

from fastapi import APIRouter

from app.database import async_session_maker
from app.users.schemas import UserResponse, UserCreate, UserLogin, TokenResponse
from app.users.services import register_user_service, login_user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register",response_model=UserResponse)
async def register_user(user:UserCreate):
    async with async_session_maker() as session:
        return await register_user_service(user,session)


@router.post("/login",response_model=TokenResponse)
async def login(user:UserLogin):
    async with async_session_maker() as session:
        return await login_user_service(user,session)
