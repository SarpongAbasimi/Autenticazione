from app.config import Config, DevelopmentConfig, TestingConfig

class TestConfigSetting():

  def test_Cofigurations(self):
    assert Config.DEBUG == False
    assert Config.TESTING == False
  
  def test_development_configurations(self):
    assert DevelopmentConfig.DEBUG == 'True'
    assert DevelopmentConfig.ENV == 'development'
  
  def test_testing_configurations(self):
    assert TestingConfig.DEBUG == 'True'