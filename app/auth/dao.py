from app.database.database import async_session
from app.database.dao.base import BaseDAO
from app.database.models import User
from sqlalchemy import select


class UserDAO(BaseDAO):
    model = User

    async def is_exists(tg_id: int, password: str):
        async with async_session() as session:
            query = select(User).where(User.tg_id == tg_id and User.password == password)
            result = await session.execute(query)
            return result.scalar_one_or_none()
