import pytest

@pytest.mark.usefixtures('client')
class TestUserPage(object):
  
  def test_user_profile_page(self, client):
    response = client.get('/altonero/chris')
    assert response.status == '302 FOUND'
  
  def test_login_users_can_see_logout_link(self, client):
    response = client.post('/auth/session',
      data =(
        {
          'email': 'c@demo.com',
          'password': 'chris',
        }),
        follow_redirects = True)
    assert b'Logout' in response.data