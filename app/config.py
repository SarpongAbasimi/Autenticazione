import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '../.env'))

class Config(object):
  DEBUG = False
  TESTING = False

class DevelopmentConfig(Config):
  ENV = os.getenv('DEVELOPMENT_ENV')
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOPMENT_DB_URI') or 'sqlite:///database/clidev.db'
  SECRET_KEY = os.getenv('SECRET_KEY')

class TestingConfig(Config):
  ENV = os.getenv('TESTING_ENV')
  TESTING = True
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.getenv('Test_DB_URI') or 'sqlite:///database/clitest.db'
  WTF_CSRF_ENABLED = False
  SECRET_KEY = os.getenv('TEST_SECRET_KEY') or 'travissecret'

config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig
}