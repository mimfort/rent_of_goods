from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

class Rental(Base):
    __tablename__ = "rentals"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(index=True)
    good_id: Mapped[int] = mapped_column(index=True)
    date_from: Mapped[date]
    date_to: Mapped[date]
    expired: Mapped[bool] = mapped_column(default=False)
