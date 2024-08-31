from app.database.dao.base import BaseDAO
from app.database.models import Subject


class SubjectDAO(BaseDAO):
    model = Subject
