from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SignUpForm(FlaskForm):

  name = StringField('name', validators=[DataRequired(), Length(min=4, max=20)])
  email = StringField('email', validators=[ DataRequired(), Email('Please enter your email address.') ])
  password = PasswordField('password', validators=[DataRequired(), Length(min=4, max=8)])
  confirm_password = PasswordField('confirm password', validators=[EqualTo('password')])
  submit = SubmitField('submit')

class LoginForm(FlaskForm):

  email = StringField('email', validators=[ DataRequired(), Email('Please a valid email address') ])
  password = PasswordField('password', validators=[ DataRequired()])
  submit = SubmitField('submit')