from flask import Flask
from app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name='development'):
  app = Flask(__name__)
  app.config.from_object(config[config_name])

  db.init_app(app)
  login_manager.init_app(app)

  from app.main.routes import main
  from app.auth.routes import auth
  from app.user.routes import user
  from app.posts.routes import posts

  app.register_blueprint(main)
  app.register_blueprint(auth, url_prefix='/auth')
  app.register_blueprint(user, url_prefix='/altonero')
  app.register_blueprint(posts, url_prefix='/altonero')

  return app