from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from config import settings


async_engine = create_async_engine(url=settings.DB_URL)
async_session = async_sessionmaker(async_engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass
