from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(100))

    #rentals = relationship("Rentals", back_populates="users")
