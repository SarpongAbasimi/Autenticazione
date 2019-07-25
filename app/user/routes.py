from flask import Blueprint, render_template

user = Blueprint('user', __name__)


@user.route('/<username>')
def profile(username):
  return render_template('profile.html',username=username)