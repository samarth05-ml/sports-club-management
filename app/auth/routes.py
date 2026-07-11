from flask_login import login_user, logout_user
from . import auth

@auth.route('/register',methods=['GET','POST'])
def register():
    return  "Registration page"

@auth.route('/login')
def login():
    return "Login Page"

@auth.route('/logout')
def logout():
    return "Logout Page"
