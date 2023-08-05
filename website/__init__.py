from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()



def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'lorem ipsum'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://okeke:abcd@localhost/biocycle'
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    db.init_app(app)

    from .veiws import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User 

    login_manager = LoginManager(app)  # Initialize LoginManager
    login_manager.login_view = 'auth.login'

    # Define the user_loader callback to load a user object based on its ID
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
        
    create_database(app)

    return app


def create_database(app):
    if not path.exists('website/'):
        db.create_all(app=app)
        print('Created Database!')
