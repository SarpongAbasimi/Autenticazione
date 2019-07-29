import pytest

@pytest.mark.usefixtures('client')
class TestMainRoutes(object):
  
  def test_home_page(self, client):
    response = client.get('/')
    assert response.status_code == 200
  
  def test_login_link_on_home_page(self, client):
    response = client.get('/')
    assert b'Login' in response.data
    assert b'Signup' in response.data