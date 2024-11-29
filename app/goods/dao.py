from typing import Literal

from app.dao.base import BaseDAO

from app.goods.models import Goods
from app.database import async_session_maker

class GoodsDAO(BaseDAO):
    model=Goods
    
    # @classmethod
    # async def update_rent_good(cls, good_id: int, status: Literal["START", "OVER"]):
    #     async with async_session_maker() as session:
    #         good = await session.query(cls.model).get(good_id)
            
    #         if good:
    #             if status == "START" and good.amount > 0:
                    
            
            