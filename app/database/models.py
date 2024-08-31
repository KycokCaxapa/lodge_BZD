from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated

from app.database.database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]


class User(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    username: Mapped[str]
    tg_id = mapped_column(BigInteger)
    password: Mapped[str]
    role: Mapped[str]


class Subject(Base):
    __tablename__ = 'subjects'

    id: Mapped[intpk]
    subject: Mapped[str]
    group: Mapped[int]
    day: Mapped[DateTime] = mapped_column(DateTime)
    place: Mapped[str]
    week: Mapped[str]
    teacher: Mapped[str]


class Homework(Base):
    __tablename__ = 'homeworks'

    id: Mapped[intpk]
    subject: Mapped[int] = mapped_column(Integer, ForeignKey('subjects.id'))
    homework: Mapped[str]
    date: Mapped[DateTime] = mapped_column(DateTime)
    author: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
