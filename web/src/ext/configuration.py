import os


def init_app(app):
    """Flask init app"""
    config = get_config_from_env()
    app.config.from_object(config)


def get_config_from_env():
    """Carrega configurações do ambiente"""
    envname = os.getenv("FLASK_ENV", "production").lower()
    if envname == "development":
        return DevelopmentConfig()
    return ProductionConfig()


class ProductionConfig:  # pylint: disable=R0903
    """PROD"""

    # FLASK
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "Ch@nG3_ME!")

    # DATABASE
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AUTH and JWT
    JWT_ISS = os.getenv("JWT_ISS", "https://confrarianews.com.br")


class DevelopmentConfig(ProductionConfig):  # pylint: disable=R0903
    """DEV"""

    FLASK_ENV = "development"
    DEBUG = True