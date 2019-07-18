import pytest
from app import create_app

@pytest.fixture(scope='class')
def client():
  app = create_app('testing')
  app_client = app.test_client()
  return app_client