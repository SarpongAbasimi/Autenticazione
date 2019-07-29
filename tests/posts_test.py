import pytest

@pytest.mark.usefixtures('client')
class TestPost(object):

  def test_posts_page(self, client):
    response = client.get('/altonero/', follow_redirects=True)
    assert b'Please log in to access this page.' in response.data

  @pytest.mark.skip(reason='I need to first login to access this page')
  def test_post_data(self, client):
    response = client.post('/altonero/create',
    data=dict(content='I love food'),
    follow_redirects=True)
    assert b'Please log in to access this page.' in response.data
