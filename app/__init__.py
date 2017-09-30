#/app/__init__.py

"""create flask app and bind to database"""

import os

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy


def create_app(config_name):
    """create app instance"""

    app = FlaskAPI(__name__, instance_relative_config=True)

    return app
