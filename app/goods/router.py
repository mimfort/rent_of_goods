from fastapi import APIRouter
from typing import Literal

from app.goods.dao import GoodsDAO
from app.goods.schemas import AddGood

router = APIRouter(
    prefix="/goods",
    tags=["Товары"]
)

@router.get("/good/{good_id}")
async def get_good(good_id: int):
    good = await GoodsDAO.find_by_id(good_id)
    
    return good


@router.post("add_good")
async def add_good(good_info: AddGood):
    new_good = GoodsDAO.add(**good_info)
    
    return new_good

@router.post("/good/rent/{status}")
async def good_rent_over(good_id: int, status: Literal["START", "OVER"]):
    good = GoodsDAO.update_rent_good(good_id) 
    # доделать обновление(забираем пользователя проверяем в зависимости от статуса какое действие делаем и выполняем обращение к бд) 