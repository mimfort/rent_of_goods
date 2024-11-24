from fastapi import FastAPI
from app.database import Base, async_engine
from app.goods.router import router as goods_router
from app.users.router import router as users_router
app = FastAPI()

@app.on_event("startup")
async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(goods_router)
app.include_router(users_router)