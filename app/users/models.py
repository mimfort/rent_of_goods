from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column

from datetime import date

class Users(Base):
    __tablename__="users"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    good_id: Mapped[int]
    date_from: Mapped[date]
    date_to: Mapped[date]
    expired: Mapped[bool]