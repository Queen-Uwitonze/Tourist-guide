import os
class Config:

    # MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:valentin@localhost/guide'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:valentin@localhost/guide'   
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}