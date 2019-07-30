from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Post

user = Blueprint('user', __name__)

@user.route('/<username>')
@login_required
def profile(username):
  user_posts = Post.query.filter_by(user=current_user).order_by(Post.id.desc())
  return render_template('profile.html',username=username, user_posts=user_posts)