from flask import Flask
from .extensions import db,bcrypt,login_manager,migrate
from .config import Config
from .auth import auth

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)


    bcrypt.init_app(app)

    login_manager.init_app(app)

    migrate.init_app(app,db)

    #Registering Blueprint
    
    app.register_blueprint(auth)
    return app
