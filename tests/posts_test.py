import pytest

@pytest.mark.usefixtures('client')
class TestPost(object):

  def test_posts_page(self, client):
    response = client.get('/altonero/', follow_redirects=True)
    assert b'Please log in to access this page.' in response.data

  # @pytest.mark.skip(reason='I need to first login to access this page')
  def test_post_data(self, client):
    
    client.post('/auth/session',
      data =(
        {
          'email': 'c@demo.com',
          'password': 'chris',
        }),
        follow_redirects = True)
    response = client.get('/altonero/')
    # response = client.post('/altonero/create',
    # data=dict(content='I love food'),
    # follow_redirects=True)
    assert b'posts page' in response.data
