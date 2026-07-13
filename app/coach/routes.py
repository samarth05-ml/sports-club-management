from flask import request,render_template
from flask_login import login_required,current_user
from .services import view_coach,assign_coach,delete_coach
from . import coach

@coach.route('/coaches',methods=['GET'])
@login_required
def viewr():
    if current_user.role!='admin':
        return " Only admin can view all coaches",403
    
    coaches=view_coach()

    return render_template("coach/view_coaches.html",coaches=coaches)

@coach.route('/assign-coach',methods=['GET','POST'])
@login_required
def assign_coachr():
    if current_user.role!='admin':
        return "only admin can assign the coach",403
    if request.method=='GET':
        return "invalid request method"
    
    user_id=request.form['user_id']
    team_id=request.form['team_id']

    return assign_coach(user_id,team_id)

@coach.route('/delete-coach',methods=['POST'])
@login_required
def delete_coachr():
    if current_user.role!='admin':
        return "Only admin can delete coach",403
    
    if request.method=='POST':
        cid=request.form['cid']

        return delete_coach(cid)
