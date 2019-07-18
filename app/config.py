import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
  DEBUG = False
  TESTING = False

class DevelopmentConfig(Config):
  ENV = os.getenv('DEVELOPMENT_ENV')
  DEBUG = os.getenv('DEVELOPMENT_DEBUG')

class TestingConfig(Config):
  ENV = os.getenv('TESTING_ENV')
  TESTING = os.getenv('IS_TESTING')
  DEBUG = os.getenv('TESTING_DEBUG')

config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig
}