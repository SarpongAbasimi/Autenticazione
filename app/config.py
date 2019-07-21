import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
  DEBUG = False
  TESTING = False

class DevelopmentConfig(Config):
  ENV = os.getenv('DEVELOPMENT_ENV')
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOPMENT_DB_URI')
  SECRET_KEY = os.getenv('SECRET_KEY')

class TestingConfig(Config):
  ENV = os.getenv('TESTING_ENV')
  TESTING = True
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.getenv('Test_DB_URI')
  WTF_CSRF_ENABLED = False
  SECRET_KEY = os.getenv('TEST_SECRET_KEY')

config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig
}