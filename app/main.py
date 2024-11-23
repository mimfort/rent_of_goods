from fastapi import FastAPI

from app.goods.router import router as goods_router

app = FastAPI()

app.include_router(goods_router)
