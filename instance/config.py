# config/config.py


import os


class Config(object):
    """Environment Configuration Class"""

    DEBUG = True
    TESTINING = False
    CSRF_TOKEN = True
    SECRET = os.getenv('SECRET_KEY')

    DB_URL = os.getenv('db_url')
    DB_USER = os.getenv('db_user')
    DB_PASSWORD = os.getenv('db_password')
    DB_PORT = os.getenv('db_port')


class DevConfig(Config):
    """Dev Environment"""
    DEBUG = True


class TestingConfig(Config):
    """Testing Environment"""
    DEBUG = True
    TESTING = True


class StagingConfig(Config):
    """Staging Environment"""
    DEBUG = True


class ProductionConfig(Config):
    """
        Production Environment, Hosted in AWS
    """
    DEBUG = False
    TESTINING = False


APP_CONFIG = {
    'dev': DevConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
