from pydantic import BaseModel

class AddGood(BaseModel):
    category_id: int
    name: str
    description: str
    price_per_day: int
    amount: int