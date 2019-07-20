import pytest

@pytest.mark.usefixtures
class TestAuth(object):
  
  def test_login_page(self, client):
    response = client.get('/auth/login')
    assert b'This is login page' in response.data
  
  def test_sign_up_page(self, client):
    response = client.get('/auth/signup')
    assert b'sign up' in response.data
  
  def test_signing_up(self, client):
    user_data = (
      { 
        'name':'chris', 
        'email':'e@demo.com',
        'password':'123',
        'confirm_password': '123'
      })
    response = client.post('/auth/signup',
    data = user_data,
    follow_redirects =True)
    assert b'chris' in response.data