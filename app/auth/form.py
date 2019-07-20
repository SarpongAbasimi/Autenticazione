from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SignUpForm(FlaskForm):

  name = StringField('name', validators=[DataRequired(), Length(min=4, max=20)])
  email = StringField('email', validators=[Email('Please enter your email address.')])
  password = PasswordField('password', validators=[DataRequired()])
  confrim_password = PasswordField('confirm password', validators=[EqualTo(password)])