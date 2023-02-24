import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

APP_ENV = os.environ.get("APP_ENV")

DB_USER = os.environ.get("MYSQL_USER")
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD")
DB_HOST = os.environ.get("MYSQL_HOST")
DB_NAME = os.environ.get("MYSQL_DATABASE")

# TODO: パスワードなどの埋め込み
ASYNC_DB_URL = "mysql+aiomysql://%s:%s@%s/%s?charset=utf8" % (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME,
)
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

Base = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session
