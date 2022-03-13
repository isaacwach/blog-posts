import os 
from dotenv import load_dotenv
load_dotenv()

class Config:
    QUOTES_API_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY=os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ayzaq:zacs@localhost/blogs'

    UPLOADS_PHOTOS_DEST ='app/static/photos'
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    
    MAIL_SERVER = 'smtp.googlegmail.com'
    SENDER_EMAIL= 'ayzaqwashyra@gmail.com'

    @staticmethod
    def init_app(app):
        pass 

class ProdConfig(Config):
    QUOTES_API_BASE_URL= os.environ.get('DATABASE_URL')

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ayzaq:zacs@localhost/blogs'
    DEBUG=True

config_options = {
    'development':DevConfig,
    'Production':ProdConfig,
    'default':ProdConfig
}
