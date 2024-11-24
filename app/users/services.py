
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.exceptions import EmailIsBusy, AuthenticationError
from app.users.auth import create_access_token
from app.users.models import Users
from app.users.schemas import UserCreate, UserResponse, UserLogin
from app.users.utils import hash_password, verify_password


async def register_user_service(user:UserCreate,db : AsyncSession) -> UserResponse:
    res = select(Users).where(Users.email == user.email)
    result = await db.execute(res)
    existing_user = result.mappings().first()
    if existing_user:
        raise EmailIsBusy
    hashed_password = hash_password(user.password)
    new_user = Users(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return UserResponse.from_orm(new_user)


async def login_user_service(user: UserLogin, db: AsyncSession) -> dict:
    result = await db.execute(select(Users).where(Users.email == user.email))
    db_user = result.scalars().first()
    print(db_user)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise AuthenticationError
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
