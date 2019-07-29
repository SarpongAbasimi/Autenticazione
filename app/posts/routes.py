from flask import Blueprint

posts = Blueprint('posts', __name__)

@posts.route('/', methods=['GET'])
def index():
  return('posts page')
