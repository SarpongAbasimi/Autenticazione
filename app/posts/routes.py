from flask import Blueprint, render_template

posts = Blueprint('posts', __name__)

@posts.route('/', methods=['GET'])
def index():
  return render_template('posts.html')
