from flask import request,render_template
from flask_login import login_required,current_user
from . import player
from .services import assign_player,view_all_players,certain_player,update_player,delete_player
from datetime import datetime

@player.route('/assign-player',methods=['GET','POST'])
@login_required
def assign_playerr():

    if current_user.role!='admin':
        return "Only admin can assign players"
    
    if request.method=='GET':
        return "should return to assign player"
    
    user_id=request.form['user_id']
    team_id=request.form['team_id']
    jersey_number=request.form['jersey_number']
    position=request.form['position']
    dob=datetime.strptime(request.form['dob'],"%Y-%m-%d").date()
    height=request.form['height']
    weight=request.form['weight']

    return assign_player(user_id=user_id,team_id=team_id,jersey_number=jersey_number,position=position,
                         dob=dob,height=height,weight=weight)

@player.route('/view-all-players',methods=['GET'])
@login_required
def view_all_playersr():
    if current_user.role not in ['admin', 'coach']:
        return "Only admin or coach can view all players"
    
    
    all_players=view_all_players()

    return render_template('players/view_all.html',allp=all_players)


@player.route('/certain_player',methods=['GET','POST'])
@login_required
def ceratin_playerr():
    if current_user.role not in ['admin', 'coach']:
        return "Only admin or coach"
    
    if request.method=='GET':
        return "again return to same page"
    
    pid=request.form['pid']

    return certain_player(pid)


@player.route('/update-player',methods=['GET','POST'])
@login_required
def update_playerr():
    if current_user.role!='admin':
        return "Only admin can update Details"
    
    if request.method=='GET':
        return "again return to same page"
    
    pid = request.form['pid']
    team_id = request.form['team_id']
    jersey_number = request.form['jersey_number']
    position = request.form['position']
    dob = request.form['dob']
    height = request.form['height']
    weight = request.form['weight']

    return update_player(pid=pid,
        team_id=team_id,
        jersey_number=jersey_number,
        position=position,
        dob=dob,
        height=height,
        weight=weight)


@player.route('/delete-player',methods=['GET','POST'])
@login_required
def delete_playerr():
    if current_user.role!='admin':
        return "Only admin can delete player"
    
    if request.method=='GET':
        return 'return same page'
    
    pid=request.form['pid']

    return delete_player(pid)



