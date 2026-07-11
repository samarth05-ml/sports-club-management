from flask import request
from flask_login import login_user,logout_user,current_user
from app.models.user import User
from app.extensions import bcrypt
from ..extensions import db

def register(username,email,password,role):
    # username=username
    # email=email
    # password=password
    # role=role

    
    roles=["admin","coach","player","medical"]

    if role not in roles:
        return "Invlaid Role"
    
    check_email=User.query.filter_by(email=email).first()
   
    if check_email:
        return "Email Already exists"
    
    hashed_password=bcrypt.generate_password_hash(password).decode("utf-8")
    user=User(username=username,email=email,password=hashed_password,role=role)
        
    db.session.add(user)
    db.session.commit()

    return " User Added Successfully "            




def login(email,password):
    email=email
    password=password

    user=User.query.filter_by(email=email).first()

    if user in None:
        return "Invalid Email"
    
    if not bcrypt.check_password_hash(user.password,password):
        return "Invalid Password"
    
    login_user(user)
    return "Login Successfull"

# if user.role == "admin":
#     return redirect(url_for("admin.dashboard"))

# elif user.role == "coach":
#     return redirect(url_for("coach.dashboard"))

# elif user.role == "player":
#     return redirect(url_for("player.dashboard"))

# elif user.role == "medical":
#     return redirect(url_for("medical.dashboard"))