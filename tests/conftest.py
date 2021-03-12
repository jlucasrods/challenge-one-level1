import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from app.config.auth import create_token, AUTH_COOKIE_NAME
from app.config.db import ModelBase, get_db
from app.main import app

TEST_DB_URL = os.getenv('TEST_DB_URL')
engine = create_engine(TEST_DB_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
ModelBase.metadata.drop_all(bind=engine)
ModelBase.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    client = TestClient(app)
    yield client


@pytest.fixture
def authorized_client(client):
    token = create_token(1)
    client.cookies.setdefault(AUTH_COOKIE_NAME, token)
    return client
