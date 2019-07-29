import pytest

@pytest.mark.usefixtures('client')
class TestPost(object):

  def test_posts_page(self):
    response = client.get('/altonero')
    assert b'posts page' in response.data