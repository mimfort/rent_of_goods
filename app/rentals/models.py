from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import date

class Rental(Base):
    __tablename__ = "rentals"

    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey("users.id"), index=True)
    good_id: int = Column(Integer, ForeignKey("goods.id"), index=True)
    date_from: date = Column(DateTime)
    date_to: date = Column(DateTime)
    expired: bool = Column(Boolean, default=False)

    user = relationship("User", back_populates="rentals")
    good = relationship("Good", back_populates="rentals")
