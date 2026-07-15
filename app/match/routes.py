from flask import request,render_template
from flask_login import login_required,current_user
from . import match
from datetime import datetime
from .services import create_match,view_all_matches,view_certain_match,update_match,delete_match

@match.route('/create-match',methods=['GET','POST'])
@login_required
def create_matchr():
    if current_user.role!='admin':
        return "Only admin can create new matches"
    
    if request.method=='GET':
        return "Return to the same page"
    
    home_team_id=request.form['home_team']
    away_team_id=request.form['away_team']
    match_date=datetime.strptime(request.form['match_date'],"%Y-%m-%d").date()
    match_time=datetime.strptime(request.form['match_time'],"%H:%M").time()
    venue=request.form['venue']

    return create_match(requested_h_id=home_team_id,requested_a_id=away_team_id,match_date=match_date,match_time=match_time,venue=venue)


@match.route('/view-all-matches',methods=['GET'])
def view_all_matchesr():
    matches=view_all_matches()
    return render_template('match/view_all_matches.html',matches=matches)

@match.route('/view-cerain-match',methods=['GET','POST'])
def view_certain_matchr():
    if request.method=='GET':
        return "return to same page"
    mid=request.form['mid']

    return view_certain_match(mid)


@match.route('/update-match-result',methods=['GET','POST'])
@login_required
def update_matchr():
    if current_user.role!='admin':
        return "Only admin can update details"
    
    if request.method=='GET':
        return "Currently this method is not implemented you need to enter mid"
    
    mid=int(request.form['mid'])
    home_score=int(request.form['home_score'])
    away_score=int(request.form['away_score'])

    return update_match(requested_mid=mid,entered_home_score=home_score,entered_away_score=away_score)


@match.route('/delete-match',methods=['GET','POST'])
@login_required
def delete_matchr():
    if current_user.role!='admin':
        return "Only admin can delete matches"
    
    if request.method=='GET':
        return "Invalid request method "
    
    mid=request.form['mid']

    return delete_match(mid)