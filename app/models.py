from app import db
from flask_login import UserMixin
from app import login_manager
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  email = db.Column(db.String(120), nullable=False)
  password = db.Column(db.String(100), nullable=False)
  post = db.relationship('Post', backref='user', lazy=True)

  def set_password(self, password):
    self.password = generate_password_hash(password)

  def check_password(self, pass_key):
    return check_password_hash(self.password, pass_key)
  
  def __repr__(self):
    return f'User {self.id} {self.name} {self.email} {self.password}'

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self):
    return f'Post => id: {self.user_id}, content: {self.content}'