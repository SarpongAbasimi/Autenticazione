from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  email = db.Column(db.String(120), nullable=False)
  password = db.Column(db.String(100), nullable=False)

  def set_password(self, password):
    self.password = generate_password_hash(password)

  def check_password(self, pass_key):
    return check_password_hash(self.password, pass_key)
  
  def __repr__(self):
    return f'User {self.id} {self.name} {self.email} {self.password}'