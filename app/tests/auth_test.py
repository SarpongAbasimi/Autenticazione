import pytest

@pytest.mark.usefixtures
class TestAuth(object):
  
  def test_login_page(self, client):
    response = client.get('/auth/login')
    assert b'This is login page' in response.data
  
  def test_sign_up_page(self, client):
    response = client.get('/auth/signup')
    assert b'sign up' in response.data