from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class SignUpForm(FlaskForm):

  name = StringField('name', validators=[DataRequired(), Length(min=4, max=20)])
  email = StringField('email', validators=[ DataRequired(), Email('Please enter your email address.') ])
  password = PasswordField('password', validators=[DataRequired(), Length(min=4, max=8)])
  confirm_password = PasswordField('confirm password', validators=[EqualTo('password')])
  submit = SubmitField('submit')

  def validate_name(self, name):
    user = User.query.filter_by(name=name.data).first()
    if user is not None:
      raise ValidationError('sorry name has alreaddy been taken.')

  def validate_email(self, email):
    email = User.query.filter_by(email=email.data).first()
    if email is not None:
      raise ValidationError('sorry email has alreaddy been taken.')

class LoginForm(FlaskForm):

  email = StringField('email', validators=[ DataRequired(), Email('Please a valid email address') ])
  password = PasswordField('password', validators=[ DataRequired()])
  submit = SubmitField('submit')