from flask import Flask
from app.controllers.pdvs import pdvs
from config import app_config
from flask_migrate import Migrate
from app.models import db


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../config.py')

    app.register_blueprint(pdvs, url_prefix='/')

    db.init_app(app)

    migrate = Migrate(app, db)

    from app import models

    return app
