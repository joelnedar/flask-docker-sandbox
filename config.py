class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    CORS_ALLOWED_ORIGINS = "productionexample.com"


class DevelopmentConfig(Config):
    DEBUG = True
    CORS_ALLOWED_ORIGINS = "developmentexample.com"


class TestingConfig(Config):
    TESTING = True
