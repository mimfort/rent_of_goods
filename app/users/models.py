from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(100), index=True)
    email: str = Column(String(100), unique=True, index=True)
    hashed_password: str = Column(String(200))

    rentals = relationship("Rental", back_populates="user")
