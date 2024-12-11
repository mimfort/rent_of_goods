from typing import Literal

from app.dao.base import BaseDAO

from app.goods.models import Goods
from app.database import async_session_maker

class GoodsDAO(BaseDAO):
    model=Goods