import pytest

@pytest.mark.usefixtures
class TestAuth(object):
  
  def test_login_page(self, client):
    response = client.get('/auth/login')
    assert b'This is login page' in response.data