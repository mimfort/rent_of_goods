from app.dao.base import BaseDAO
from app.rentals.models import Rentals


class RentalsDAO(BaseDAO):
    model=Rentals