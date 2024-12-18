from pydantic import BaseModel

from datetime import date

class SRent(BaseModel):
    id: int
    user_id: int
    good_id: int
    date_from: date
    date_to: date
    expired: bool