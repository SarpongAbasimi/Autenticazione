from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  email = db.Column(db.String(120), nullable=False)
  password = db.Column(db.String(100), nullable=False)
  
  def __repr__(self):
    return f'User {self.id} {self.name} {self.email}'