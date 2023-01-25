import os

from sqlalchemy import create_engine

from api.models.task import Base

DB_PASSWORD = os.environ.get("MYSQL_PASSWORD")
DB_HOST = os.environ.get("MYSQL_HOST")
DB_PORT = os.environ.get("MYSQL_PORT")
DB_NAME = os.environ.get("MYSQL_DATABASE")

# TODO: パスワードなどの埋め込み
DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
# DB_URL = "mysql+pymysql://root:root@db:3306/demo?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
