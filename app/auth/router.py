from fastapi import APIRouter, Response

from app.auth.dao import UserDAO
from app.auth.services import create_jwt, get_password_hash
from app.auth.schemas import SRegistration
from app.exceptions import *


router = APIRouter(prefix='/auth',
                   tags=['Authentication'])


@router.post('/registration')
async def registration(data: SRegistration):
    user = await UserDAO.get_by_filter(tg_id=data.tg_id)
    if user:
        raise UserAlreadyExists
    hashed_password = get_password_hash(data.password)
    await UserDAO.create(username=data.username,
                      tg_id=data.tg_id,
                      password=hashed_password,
                      role='Студент')
    return user


@router.post('/login')
async def login(response: Response, data: SRegistration):
    user = await UserDAO.is_exists(data.tg_id, data.password)
    if not user:
        return UserDoesNotExists
    jwt = create_jwt({'sub': str(user.id)})
    response.set_cookie('jwt', jwt, httponly=True)
