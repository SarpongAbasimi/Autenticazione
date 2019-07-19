from app.config import Config, DevelopmentConfig, TestingConfig

class TestConfigSetting():

  def test_Cofigurations(self):
    assert Config.DEBUG == False
    assert Config.TESTING == False
  
  def test_development_configurations(self):
    db_uri = hasattr(DevelopmentConfig, 'SQLALCHEMY_DATABASE_URI')
    assert DevelopmentConfig.DEBUG == 'True'
    assert DevelopmentConfig.ENV == 'development'
    assert db_uri == True
  
  def test_testing_configurations(self):
    assert TestingConfig.DEBUG == 'True'