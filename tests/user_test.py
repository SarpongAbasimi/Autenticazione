import pytest

@pytest.mark.usefixtures('client')
class TestUserPage(object):
  
  def test_user_profile_page(self, client):
    response = client.get('/altonero/chris')
    assert response.status == '302 FOUND'