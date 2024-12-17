from datetime import datetime, timedelta, timezone
from app.config import settings
from jose import jwt

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data : dict):
    to_encode = data.copy()
    expire = (datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)).timestamp()
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(key = SECRET_KEY, algorithm=ALGORITHM,claims=to_encode)
    return encoded_jwt




