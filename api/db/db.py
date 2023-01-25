import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_PASSWORD = os.environ.get("MYSQL_PASSWORD")
DB_HOST = os.environ.get("MYSQL_HOST")
DB_PORT = os.environ.get("MYSQL_PORT")
DB_NAME = os.environ.get("MYSQL_DATABASE")

# TODO: パスワードなどの埋め込み
ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8"
# ASYNC_DB_URL = "mysql+aiomysql://root:root@db:3306/demo?charset=utf8"
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

Base = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session
