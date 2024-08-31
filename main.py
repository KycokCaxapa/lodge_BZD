from fastapi import FastAPI

import asyncio

from app.auth.router import router as auth_router
from app.schedule.router import router as schedule_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(schedule_router)


@app.get('/')
async def main():
    return None


if __name__ == '__main__':
    asyncio.run(main())
