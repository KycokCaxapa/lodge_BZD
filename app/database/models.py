from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    tg: Mapped[str]
    password: Mapped[str]
    role: Mapped[str]


class Schedule(Base):
    __tablename__ = 'schedule'

    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str]
    place: Mapped[str]
    week: Mapped[str]
    teacher: Mapped[str]


class Homework(Base):
    __tablename__ = 'homeworks'

    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(Integer, ForeignKey('schedule.id'))
    homework: Mapped[str]
    date: Mapped[DateTime] = mapped_column(DateTime)
    author: Mapped[str] = mapped_column(Integer, ForeignKey('users.id'))
