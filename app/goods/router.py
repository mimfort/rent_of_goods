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


@router.post("/add_good")
async def add_good(good_info: AddGood):
    try:
        new_good = await GoodsDAO.add(**dict(good_info))
    except Exception:
        return "Ошибка"
    
    return new_good

@router.post("/good/rent/{status}")
async def good_rent_status(good_id: int, status: Literal["START", "OVER"]):
    good_amount = await GoodsDAO.find_by_id(good_id)

    if status == "START" and good_amount.amount > 0:
        good = await GoodsDAO.update(id=good_id, field="amount", data=good_amount.amount - 1)
    else:
        good = await GoodsDAO.update(id=good_id, field="amount", data=good_amount.amount + 1)
        
    return True