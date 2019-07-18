from flask import Flask
from app.config import config

def create_app(config_name='development'):
  app = Flask(__name__)
  app.config.from_object(config[config_name])

  return app