import os

from sqlalchemy import create_engine

from api.models.task import Base

APP_ENV = os.environ.get('APP_ENV')

DB_USER = os.environ.get('MYSQL_USER')
DB_PASSWORD = os.environ.get('MYSQL_PASSWORD')
DB_HOST = os.environ.get('MYSQL_HOST')
DB_NAME = os.environ.get('MYSQL_DATABASE')

DB_URL = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME,
)
print(DB_URL)
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
