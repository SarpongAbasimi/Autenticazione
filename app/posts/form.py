from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
  content = TextAreaField('content', validators=[DataRequired()])
  submit = SubmitField('Post', validators=[DataRequired()])