import pytest

@pytest.mark.usefixtures('client')
class TestMainRoutes(object):
  
  def test_home_page(self, client):
    response = client.get('/')
    assert response.status_code == 200