from fastapi import APIRouter

from app.categories.dao import CategoriesDAO

router = APIRouter(
    prefix="/categories",
    tags=["Категории"]
)

@router.get("/category/{category_id}")
async def get_category_by_id(category_id: int):
    category = await CategoriesDAO.find_by_id(category_id)
    
    return category

@router.post("/add_category")
async def add_category(name: str, description: str = ''):
    res = CategoriesDAO.add(name=name, description=description)
    
    return res

# @router.post("/update_category/{category_id}")
# async def update_category(category_id: int):
#     pass