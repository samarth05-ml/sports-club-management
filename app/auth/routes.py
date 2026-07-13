from flask_login import login_user, logout_user,login_required
from flask import request,render_template,redirect,url_for
from . import auth
from .services import login,register

@auth.route('/register',methods=['GET','POST'])
def registerr():
    if request.method=='GET':
        return  "Registration page"
    elif request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        role=request.form['role']

        return register(username,email,password,role)
  

@auth.route('/login',methods=['GET','POST'])
def loginr():
    if request.method=='GET':
        return "should return login.html"
    elif request.method=='POST':
            email = request.form["email"]
            password = request.form["password"]
            return login(email,password)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))