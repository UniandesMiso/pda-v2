class Config(object): ...


class ProductionConfig(Config):
    TESTING = False


class DevelopmentConfig(Config):
    TESTING = True


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
}
