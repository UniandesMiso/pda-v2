from os import environ


class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://"
        + f"{environ.get('DB_USER')}:{environ.get('DB_PASS')}@"
        + f"{environ.get('DB_HOST')}:{environ.get('DB_PORT')}/"
        + f"{environ.get('DB_NAME')}"
    )


class DevelopmentConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
}
