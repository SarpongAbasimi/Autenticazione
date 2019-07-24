import pytest, os
from app import create_app, db
from app.models import User

@pytest.fixture(scope='class')
def client():
  app = create_app('testing')
  app.app_context().push()
  app_client = app.test_client()

  db.create_all()

  seed_user = User(name='chris', email='c@demo.com')
  seed_user.set_password('chris')
  db.session.add(seed_user)
  db.session.commit()
  
  yield app_client

  db.drop_all()

