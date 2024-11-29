from fastapi import APIRouter

from app.config import settings
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