from fastapi import APIRouter

from app.config import settings

router = APIRouter(
    prefix="/goods",
    tags=["Товары"]
)


@router.get("/hello")
async def say_hello():
    return settings.DATABASE_URL