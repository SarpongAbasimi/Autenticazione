class Config(object):
  DEBUG = False
  TESTING = False

class DevelopmentConfig(Config):
  ENV = 'development'
  DEBUG = True

class TestingConfig(Config):
  DEBUG = True

config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig
}