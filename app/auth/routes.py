from flask_login import login_user, logout_user,login_required,current_user
from flask import request,render_template,redirect,url_for
from . import auth
from .services import login,register

@auth.route('/register',methods=['GET','POST'])
def registerr():
    if request.method=='GET':
        return  render_template('auth/register.html')
    elif request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        role=request.form['role']

        return register(username,email,password,role)
  

@auth.route('/login',methods=['GET','POST'])
def loginr():
    if request.method=='GET':
        return render_template('auth/login.html')
    elif request.method=='POST':
            email = request.form["email"]
            password = request.form["password"]
            return login(email,password)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/admin-dashboard',methods=['GET','POST'])
@login_required
def admin_dashboard():
     if current_user.role=='admin':
          return render_template(auth/admin_dashboard.html)
