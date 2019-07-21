import pytest

@pytest.mark.usefixtures
class TestAuth(object):
  
  def test_login_page(self, client):
    response = client.get('/auth/login')
    assert b'This is login page' in response.data
  
  def test_sign_up_page(self, client):
    response = client.get('/auth/signup')
    assert b'sign up' in response.data

  def test_signing_up_error_validation(self, client):
    user_data = (
      { 
        'name':'c', 
        'email':'e.com',
        'password':'123',
        'confirm_password': '123'
      })
    response = client.post('/auth/signup',
    data = user_data,
    follow_redirects =True)
    assert b'Field must be between 4 and 20 characters long.' in response.data
    assert b'Please enter your email address.' in response.data