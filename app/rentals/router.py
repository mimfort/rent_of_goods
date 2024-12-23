from fastapi import APIRouter, Depends
from datetime import date
from pydantic import TypeAdapter

from app.users.models import Users
from app.exceptions import TokenAbsentException, IncorrectDateException, LackOfGoodException
from app.users.dependencies import get_current_user
from app.rentals.dao import RentalsDAO
from app.goods.dao import GoodsDAO
from app.rentals.schemas import SRent
from app.goods.schemas import SGood
from app.tasks.tasks import email_rent_confirm

router = APIRouter(
    prefix="/rent",
    tags=["Аренда"]
)

@router.get("/my_rents")
async def get_my_rents(user: Users = Depends(get_current_user)):
    rents = await RentalsDAO.find_all(user_id=user.id)
    if not rents:
        return "У вас нет арендованных товаров"
    
    return rents

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
        
        upd_good = await GoodsDAO.update(id=good_id, field="amount", data=good_amount.amount - 1)
        
        rent_for_celery = {
            "date_from": new_rent.date_from,
            "date_to": new_rent.date_to
        }
        
        upd_for_celery = {
            "name": upd_good.name,
            "price_per_day": upd_good.price_per_day
        }
        email_rent_confirm.delay(rent_for_celery, upd_for_celery, user.email)
        
        return new_rent
    else:
        raise LackOfGoodException

@router.delete("/delete_rent/{rent_id}")
async def delete_rent(rent_id: int, user: Users = Depends(get_current_user)):
    if user:
        rent = await RentalsDAO.find_by_id(rent_id)

        await RentalsDAO.delete(id=rent_id)

        good = await GoodsDAO.find_by_id(rent.good_id)
        await GoodsDAO.update(rent.good_id, "amount", good.amount + 1)
    else:
        raise TokenAbsentException