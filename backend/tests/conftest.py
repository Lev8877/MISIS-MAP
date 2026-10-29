import pytest
import asyncio
import json

from main import app

from fastapi.testclient import TestClient

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.pool import NullPool

import os
from dotenv import load_dotenv

from dependencies import get_session

from database import Base

from import_data import import_data


load_dotenv()

engine = create_async_engine(os.getenv('TEST_DATABASE_URL'), poolclass=NullPool)

TestSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


async def override_get_session():
    async with TestSessionLocal() as session:
        yield session


async def prepare_database():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

    with open('data.json', encoding='utf-8') as file:
        data = json.load(file)

    async with TestSessionLocal() as session:
        await import_data(session=session, data=data)


@pytest.fixture(scope='session', autouse=True)
def database():
    asyncio.run(prepare_database())


@pytest.fixture
def client():
    app.dependency_overrides[get_session] = override_get_session
    return TestClient(app)
