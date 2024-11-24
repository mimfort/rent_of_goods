from sqlalchemy import Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base
from datetime import date

class Rentals(Base):
    __tablename__ = "rentals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), index=True)
    good_id: Mapped[int] = mapped_column(Integer, ForeignKey("goods.id"), index=True)
    date_from: Mapped[date] = mapped_column(DateTime)
    date_to: Mapped[date] = mapped_column(DateTime)
    expired: Mapped[bool] = mapped_column(Boolean, default=False)

    #user = relationship("Users", back_populates="rentals")
    #good = relationship("Goods", back_populates="rentals")
