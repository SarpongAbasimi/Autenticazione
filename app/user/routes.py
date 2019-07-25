from flask import Blueprint, render_template
from flask_login import login_required

user = Blueprint('user', __name__)

@user.route('/<username>')
@login_required
def profile(username):
  return render_template('profile.html',username=username)