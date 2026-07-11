from flask import Flask
from .extensions import db,bcrypt,login_manager,migrate
from .config import Config
from .auth import auth
from .models.user import User

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)


    bcrypt.init_app(app)

    login_manager.init_app(app)

    migrate.init_app(app,db)

    #Registering Blueprint
    
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(int(uid))
    
    app.register_blueprint(auth)
    return app
