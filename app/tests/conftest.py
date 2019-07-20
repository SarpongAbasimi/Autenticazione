import pytest, os
from app import create_app, db

@pytest.fixture(scope='class')
def client():
  app = create_app('testing')
  app.app_context().push()
  app_client = app.test_client()

  db.create_all()

  yield app_client

  db.drop_all()