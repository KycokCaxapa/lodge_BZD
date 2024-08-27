from fastapi import APIRouter, HTTPException, Response

from app.auth.services import create_jwt, get_password_hash
from app.auth.schemas import SRegistration
from app.exceptions import *


router = APIRouter(prefix='/auth',
                   tags=['Authentication'])


@router.get('/registration')
async def registration(data: SRegistration):
    user = await UserDAO.get_by_filter(tg=data.tg)
    if user:
        raise UserAlreadyExists
    hashed_password = get_password_hash(data.password)
    await UserDAO.add(username=data.username,
                      tg=data.tg,
                      password=hashed_password)


@router.post('/login')
async def login(response: Response, data: SRegistration):
    user = await UserDAO.is_exists(data.tg, data.password)
    if not user:
        return UserDoesNotExists
    jwt = create_jwt({'sub': str(user.id)})
    response.set_cookie('JWT', jwt, httponly=True)
