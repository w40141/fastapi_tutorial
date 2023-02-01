import pytest
import starlette.status
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from api.db.db import Base, get_db
from api.main import app

ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture
async def async_client() -> AsyncClient:
    # Async用のengineとsessionを作成
    async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
    async_session = sessionmaker(
        autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
    )

    # テスト用にオンメモリのSQLiteテーブルを初期化（関数ごとにリセット）
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # DIを使ってFastAPIのDBの向き先をテスト用DBに変更
    async def get_test_db():
        async with async_session() as session:
            yield session

    app.dependency_overrides[get_db] = get_test_db

    # テスト用に非同期HTTPクライアントを返却
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_create_and_read(async_client):
    responses = await async_client.post("/tasks", json={"title": "Test Task"})
    assert responses.status_code == starlette.status.HTTP_200_OK
    responses_obj = responses.json()
    assert responses_obj["title"] == "Test Task"

    responses = await async_client.get("/tasks")
    assert responses.status_code == starlette.status.HTTP_200_OK
    responses_obj = responses.json()
    assert len(responses_obj) == 1
    assert responses_obj[0]["title"] == "Test Task"
    assert responses_obj[0]["done"] is False


@pytest.mark.asyncio
async def test_done_flag(async_client):
    responses = await async_client.post("/tasks", json={"title": "Test Task 2"})
    assert responses.status_code == starlette.status.HTTP_200_OK
    responses_obj = responses.json()
    assert responses_obj["title"] == "Test Task 2"

    # 完了フラグを立てる
    responses = await async_client.put("/tasks/1/done")
    assert responses.status_code == starlette.status.HTTP_200_OK

    # 既に完了フラグが立っているので400を返す
    responses = await async_client.put("/tasks/1/done")
    assert responses.status_code == starlette.status.HTTP_400_BAD_REQUEST

    # 完了フラグを外す
    responses = await async_client.delete("/tasks/1/done")
    assert responses.status_code == starlette.status.HTTP_200_OK

    # 既に完了フラグが外れているので404を返す
    responses = await async_client.delete("/tasks/1/done")
    assert responses.status_code == starlette.status.HTTP_404_NOT_FOUND
