from app.models import User

class TestModel(object):

  def test_user_has_id_attr(self):
    id = hasattr(User, 'id')
    assert id == True
  
  def test_user_has_name_attr(self):
    name = hasattr(User, 'name')
    assert name == True
  
  def test_user_has_email_arrt(self):
    email = hasattr(User, 'email')
    assert email == True
  
  def test_user_has_password_attr(self):
    password = hasattr(User, 'password')
    assert password == True