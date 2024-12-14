from fastapi import HTTPException

from fastapi import APIRouter
from fastapi.params import Depends

from app.categories.dao import CategoriesDAO
from app.exceptions import TokenAbsentException
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/categories",
    tags=["Категории"]
)

@router.get("/category/{category_id}")
async def get_category_by_id(category_id: int):
    category = await CategoriesDAO.find_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return category

@router.post("/add_category")
async def add_category(name: str, description: str = '',user: Users = Depends(get_current_user)):
    if not user:
        raise TokenAbsentException
    res = await CategoriesDAO.add(name=name, description=description)
    return res

@router.post("/update_category/{category_id}")
async def update_category(category_id: int):
    pass