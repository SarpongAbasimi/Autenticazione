import os
from dotenv import load_dotenv

basedir = os.path.dirname(os.path.abspath(__file__))
load_dotenv()

class Config(object):
  DEBUG = False
  TESTING = False

class DevelopmentConfig(Config):
  ENV = os.getenv('DEVELOPMENT_ENV')
  DEBUG = os.getenv('DEVELOPMENT_DEBUG')
  SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOPMENT_DB_URI') or 'sqlite:///database/de.db'

class TestingConfig(Config):
  ENV = os.getenv('TESTING_ENV')
  TESTING = os.getenv('IS_TESTING')
  DEBUG = os.getenv('TESTING_DEBUG')
  SQLALCHEMY_DATABASE_URI = os.getenv('Test_DB_URI')

config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig
}