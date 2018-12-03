class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@172.28.1.2/pdv'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


# CASO HAJA DEV / PROD CONFIG
app_config = {
    'development': DevelopmentConfig
}
