from datetime import datetime, timedelta, timezone
from app.config import settings
import jwt

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data : dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc).timestamp() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(payload=to_encode,key = SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




