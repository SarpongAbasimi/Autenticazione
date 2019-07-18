import pytest
from app import create_app
from app.config import config

@pytest.fixture(scope='class')
def client():
  app = create_app(config['testing'])
  app.app.test_client()
  return app