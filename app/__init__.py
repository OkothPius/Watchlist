from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
# from . import views,forms

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'





bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
Mail = Mail()


def create_app(config_name):

    app = Flask(__name__)
    #Create a login view
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # configure UploadSet
    configure_uploads(app,photos)

    #Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # setting config
    from .request import configure_request
    configure_request(app)




    return app
