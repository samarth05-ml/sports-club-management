from flask import request,render_template
from . import training
from datetime import datetime
from flask_login import login_required,current_user
from .services import create_training,view_all_sessions,view_session
@training.route('/create-training',methods=['GET','POST'])
@login_required
def create_trainingr():
    if current_user.role not in['admin','coach']:
        return "Only Admin or Coach can create Training sessions"
    
    if request.method=='GET':
        return "again return to same page"
    
    team_id=request.form['team_id']
    cid=current_user.coach.cid
    title=request.form['title']
    description=request.form['description']
    date=datetime.strptime(request.form['date'],"%Y-%m-%d").date()
    start_time = datetime.strptime(request.form["start_time"],"%H:%M").time()
    end_time = datetime.strptime(request.form["end_time"],"%H:%M").time()
    location=request.form['location']

    return create_training(
    team_id=team_id,
    cid=cid,
    title=title,
    description=description,
    date=date,
    start_time=start_time,
    end_time=end_time,
    location=location)

@training.route('/view-all-sessions',methods=['GET'])
@login_required
def view_all_sessionsr():
    if current_user.role!='admin':
        return "Only admin have acces to view all training session"
    
    if request.method=='GET':
        view_all=view_all_sessions()
        return render_template('training/view_all.html',view_all=view_all)
    

@training.route('/view-specific',methods=['GET','POST'])
@login_required
def view_specificr():
    if current_user.role not in['coach','player']:
        return "Only coaches and players can view their training sessions"
    team_id = int(request.form['team_id'])
    return view_session(team_id,current_user.tid)