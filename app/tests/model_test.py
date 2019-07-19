from app.models import User

class TestModel(object):

  def test_user_has_id(self):
    id = hasattr(User, 'id')
    assert id == True