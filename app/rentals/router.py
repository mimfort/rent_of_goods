from fastapi import APIRouter, Depends
from datetime import date

from app.users.models import Users
from app.exceptions import TokenAbsentException, IncorrectDateException, LackOfGoodException
from app.users.dependencies import get_current_user
from app.rentals.dao import RentalsDAO
from app.goods.dao import GoodsDAO

router = APIRouter(
    prefix="/rent",
    tags=["Аренда"]
)
@router.get("/my_rents")
async def get_my_rents(user: Users = Depends(get_current_user)):
    rents = await RentalsDAO.find_all(user_id=user.id)
    
    
@router.post("/add_rent")
async def add_rent(good_id: int,
                   date_from: date,
                   date_to: date,
                   expired: bool,
                   user: Users = Depends(get_current_user)):
    if not user:
        raise TokenAbsentException
    
    if date_from > date_to:
        raise IncorrectDateException
    
    good_amount = await GoodsDAO.find_by_id(good_id)
    
    if good_amount and good_amount.amount > 0:
    
        new_rent = await RentalsDAO.add(
            user_id=user.id,
            good_id=good_id,
            date_from=date_from,
            date_to=date_to,
            expired=expired
        )
        
        await GoodsDAO.update(id=good_id, field="amount", data=good_amount.amount - 1)
    else:
        raise LackOfGoodException
