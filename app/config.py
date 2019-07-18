import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
  DEBUG = False
  TESTING = False

class DevelopmentConfig(Config):
  ENV = os.getenv('DEVELOPMENT_ENV')
  DEBUG = True

class TestingConfig(Config):
  DEBUG = True

config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig
}