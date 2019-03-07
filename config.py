import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:wito@localhost/tourist_guide'
    MAP_API_BASE_URL ='https://maps.googleapis.com/maps/api/js?key=YOUR_KEY&callback=myMap'
    MAP_API_KEY = os.environ.get('MAP_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}