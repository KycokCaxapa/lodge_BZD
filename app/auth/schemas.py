from pydantic import BaseModel
from enum import Enum


class Role(str, Enum):
    student = 'студент'
    elder = 'староста'


class SRegistration(BaseModel):
    username: str
    tg_id: int
    password: str
    role: Role
