from fastapi import HTTPException, status


UserAlreadyExists = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Пользователь уже существует')

UserDoesNotExists = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Пользователь не существует')
