from fastapi import APIRouter

router = APIRouter(
    prefix="/goods",
    tags=["Товары"]
)


@router.get("/hello")
async def say_hello():
    return "Hello"