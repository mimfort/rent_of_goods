from fastapi import FastAPI
from app.database import Base, async_engine
from app.goods.router import router as goods_router
from app.users.router import router as users_router
from app.categories.router import router as categories_router
app = FastAPI()


app.include_router(goods_router)
app.include_router(users_router)
app.include_router(categories_router)