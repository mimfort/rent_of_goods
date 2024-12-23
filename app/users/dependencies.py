from jose import jwt, JWTError
from fastapi import Request, Depends
from datetime import datetime, timezone

from app.exceptions import TokenAbsentException
from app.config import settings
from app.exceptions import *
from app.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise TokenAbsentException
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.HASH_ALGO
        )
    except JWTError:
        raise IncorrectTokenFormatException

    expire: str = payload.get("exp")
    if not expire or (int(expire) < datetime.now(timezone.utc).timestamp()):
        raise ExpiredTokenException
    
    user_email: str = payload.get("sub")
    if not user_email:
        raise UserIsNotPresentException

    user = await UsersDAO.find_one_or_none(email=user_email)
    if not user:
        raise UserIsNotPresentException

    return user
