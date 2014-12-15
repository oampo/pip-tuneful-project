class DevelopmentConfig(object):
    DATABASE_URI = "sqlite:///tuneful-development.db"
    DEBUG = True
    UPLOAD_FOLDER = "uploads"

class TestingConfig(object):
    DATABASE_URI = "sqlite://"
    DEBUG = True
    UPLOAD_FOLDER = "test-uploads"
