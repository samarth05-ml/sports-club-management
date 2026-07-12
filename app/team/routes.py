from flask_login import login_user ,current_user,login_required
from ..models.teams import Team
from . import team
from flask import request,render_template
from .services import create_team,view_team,delete_team


@team.route('/teams',methods=['GET','POST'])
@login_required
def create_teamr():
    if current_user.role!='admin':
        return "Only Admins can create team",403
    
    if request.method=='GET':
        return " ... "
    elif request.method=='POST':
        team_name=request.form['team_name']
        city=request.form['city']

        message=create_team(team_name,city)
        return message
    
@team.route('/view_teams',methods=['GET'])
def view_teamr():
    if request.method=='POST':
        return "Invalid Request Method"
    elif request.method=='GET':
        team=view_team()
        return render_template("team/view_teams.html",teams=team)
        
@team.route('/delete_team',methods=['GET','POST'])
@login_required
def delete_teamr():
    if current_user.role!='admin':
        return "Only admin can delete Teams"
    
    if request.method=='GET':
        return "Invalid request method"
    elif request.method=='POST':
        del_team=request.form['delete_team']

        message=delete_team(del_team)
        return message
    