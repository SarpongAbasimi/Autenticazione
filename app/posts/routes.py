from flask import Blueprint, render_template
from .form import PostForm
from flask_login import login_required

posts = Blueprint('posts', __name__)

@posts.route('/', methods=['GET'])
@login_required
def index():
  postform = PostForm()
  return render_template('posts.html', postform=postform)