from flask import Flask
from app.config import config


def create_app(config_name='development'):
  app = Flask(__name__)
  app.config.from_object(config[config_name])

  from app.main.routes import main
  app.register_blueprint(main)
  return app