from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from flask_login import current_user
from app.models import Post
from .form import PostForm
from app import db

posts = Blueprint('posts', __name__)

@posts.route('/', methods=['GET'])
@login_required
def index():
  postform = PostForm()
  return render_template('posts.html', postform=postform)

@posts.route('/create', methods=['POST'])
def create():
  postform = PostForm()
  if request.method == 'POST' and postform.validate_on_submit():
    post = Post(content=postform.content.data, user=current_user)
    db.session.add(post)
    db.session.commit()
    flash('Tweep posted')
    postform.content.data = ''
    return redirect(url_for('posts.index'))
  return redirect(url_for('posts.index'))

