from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class Week(str, Enum):
    even = 'Чётный'
    odd = 'Нечётный'


class SSubject(BaseModel):
    subject: str
    group: int
    day: datetime
    place: str
    week: Week
    teacher: str
