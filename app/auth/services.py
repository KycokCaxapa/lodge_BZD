from passlib.context import CryptContext
from jose import jwt

from datetime import datetime, timezone, timedelta

from app.auth.dao import UserDAO
from config import settings


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password, hashed_password) -> bool:
    return pwd_context.verify(password, hashed_password)


def create_jwt(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode,
                             settings.JWT_KEY,
                             algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt
