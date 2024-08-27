from pydantic import BaseModel


class SRegistration(BaseModel):
    username: str
    tg: int
    password: str
