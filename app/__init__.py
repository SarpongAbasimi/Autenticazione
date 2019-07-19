from flask import Flask
from app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='development'):
  app = Flask(__name__)
  app.config.from_object(config[config_name])

  db.init_app(app)

  from app.main.routes import main
  from app.auth.routes import auth


  app.register_blueprint(main)
  app.register_blueprint(auth, url_prefix='/auth')

  return app