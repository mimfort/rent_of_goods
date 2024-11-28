from fastapi import HTTPException, status
EmailIsBusy = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Почта уже занята!")
AuthenticationError = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Ошибка авторизации")
TokenAbsentException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не обнаружен")