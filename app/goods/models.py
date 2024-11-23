from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Good(Base):
    __tablename__ = "goods"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(100), index=True)
    description: str = Column(String(200))
    price_per_day: int = Column(Integer)
    available: bool = Column(Boolean, default=True)
    category_id: int = Column(Integer, ForeignKey("categories.id"), nullable=True)
    category = relationship("Category", back_populates="goods")
