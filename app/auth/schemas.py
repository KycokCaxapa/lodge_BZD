from pydantic import BaseModel
from enum import Enum


class Role(str, Enum):
    student = 'Студент'
    elder = 'Староста'


class SRegistration(BaseModel):
    username: str
    tg_id: int
    password: str
    role: Role
