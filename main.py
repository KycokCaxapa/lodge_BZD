from fastapi import FastAPI

import asyncio

from app.auth.router import router as auth_router


app = FastAPI()
app.include_router(auth_router)


@app.get('/')
async def main():
    return None


if __name__ == '__main__':
    asyncio.run(main())
