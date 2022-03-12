from flask import Flask
from config import DevConfig
from config import config_options
from flask_uploads import IMAGES, UploadSet,configure_uploads
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import os
from flask_bootstrap import Bootstrap

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db=SQLAlchemy()
mail=Mail()
login_manager=LoginManager()
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)
login_manager.session_protection = 'strong'

def create_app(config_name):
    app= Flask(__name__)

    # Creating the app configurations
    #app.config.from_object(config_options[config_name])
   #config_name = os.getenv('FLASK_CONFIG') or 'default'
    from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint
    # Registering the blueprint
    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(main_blueprint)
    app.config['UPLOADS_DEFAULT_DEST']='app/static/photos'
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['QUOTES_API_BASE_URL']='http://quotes.stormconsultancy.co.uk/random.json'

    login_manager.init_app(app)
    configure_uploads(app,photos)
    db.init_app(app)
    #mail.init_app(app)
    bootstrap.init_app(app)

    with app.app_context():
        db.create_all()

    return app 