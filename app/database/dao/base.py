from sqlalchemy import insert, select

from app.database.database import async_session


class BaseDAO:
    model = None

    @classmethod
    async def get_by_id(cls, id: int):
        async with async_session() as session:
            object = await session.scalar(select(cls.model).where(cls.id == id))
            return object
    
    @classmethod
    async def get_by_filter(cls, **filter):
        async with async_session() as session:
            object = await session.scalar(select(cls.model).filter_by(**filter))
            return object
    
    @classmethod
    async def add(cls, **data):
        async with async_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
