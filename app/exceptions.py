from fastapi import HTTPException, status
EmailIsBusy = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Почта уже занята!")
AuthenticationError = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Ошибка авторизации")
TokenAbsentException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не обнаружен")
# новые
IncorrectTokenFormatException = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Неправильный формат токена")
ExpiredTokenException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен недействителен")
UserIsNotPresentException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не обнаружен")
IncorrectDateException = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Неверно введены даты")
LackOfGoodException = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Данный товар отсутствует")