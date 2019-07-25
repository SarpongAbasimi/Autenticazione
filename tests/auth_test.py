import pytest

@pytest.mark.usefixtures
class TestAuth(object):
  
  def test_login_page(self, client):
    response = client.get('/auth/login')
    assert b'This is login page' in response.data
  
  def test_login_session(self, client):
    response = client.post('/auth/session',
      data =(
        {
          'email': 'e@demo.com',
          'password': '123456',
        }),
        follow_redirects = True)
    assert b'Invalid email or password.' in response.data
  
  def test_sign_up_page(self, client):
    response = client.get('/auth/signup')
    assert b'sign up' in response.data

  def test_signing_up_error_validation(self, client):
    user_data = (
      { 
        'name':'c',
        'email':'e.com',
        'password':'de',
        'confirm_password': '123'
      })
    response = client.post('/auth/signup',
    data = user_data,
    follow_redirects =True)
    assert b'Field must be between 4 and 20 characters long.' in response.data
    assert b'Please enter your email address.' in response.data
    assert b'Field must be between 4 and 8 characters long.' in response.data
    assert b'Field must be equal to password.' in response.data

  def test_for_correct_registration(self, client):
    user_data = (
      { 
        'name':'hris',
        'email':'e@demo.com',
        'password':'123456',
        'confirm_password':'123456'
      })
    response = client.post('/auth/signup',
    data = user_data,
    follow_redirects =True)
    assert b'You were successfully registered.' in response.data

  def test_name_validation_error_duplicate_email(self, client):
    response = client.post('/auth/signup',
    data= {
      'name': 'chris',
      'email': 'ca@demo.com',
      'password': 'sam'
    },
    follow_redirects=True)
    assert b'sorry name has alreaddy been taken.' in response.data
  
  def test_email_validation_error_duplicate(self, client):
    response = client.post('/auth/signup',
    data= {
      'name': 'nas',
      'email': 'c@demo.com',
      'password': 'sam'
    },
    follow_redirects=True)
    assert b'sorry email has alreaddy been taken.' in response.data

  def test_email_name_validation_error_works(self, client):
    response = client.post('/auth/signup',
    data= {
      'name': 'chris',
      'email': 'c@demo.com',
      'password': 'sam'
    },
    follow_redirects=True)
    assert b'sorry name has alreaddy been taken.' in response.data
    assert b'sorry email has alreaddy been taken.' in response.data
  
  def test_for_nav_links_on_login_page(self, client):
    response = client.get('/auth/login')
    assert b'Home' in response.data 