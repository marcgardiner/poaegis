#/app/__init__.py

"""create flask app and bind to database"""

import os


from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy


from instance.config import APP_CONFIG


db = SQLAlchemy()


def create_app(config_name):
    """create app instance"""

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    return app
