from sqlalchemy import insert, select, update

from app.database.database import async_session


class BaseDAO:
    model = None
    
    @classmethod
    async def create(cls, **data) -> None:
        async with async_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_by_id(cls, id: int):
        async with async_session() as session:
            object = await session.scalar(select(cls.model).where(cls.id == id))
            return object
    
    @classmethod
    async def get_by_filter(cls, **filter):
        async with async_session() as session:
            object = await session.scalars(select(cls.model).filter_by(**filter))
            return object
    
    @classmethod
    async def update(cls, id: int, **kwargs) -> None:
        async with async_session() as session:
            await session.execute(update(cls.model).where(cls.model.id == id).values(**kwargs))
            await session.commit()

    @classmethod
    async def delete_by_filter(cls, **filter) -> None:
        async with async_session() as session:
            object = await session.scalar(select(cls.model).filter_by(**filter))
            await session.delete(object)
            await session.commit()
