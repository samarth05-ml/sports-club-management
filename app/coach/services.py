from ..models.coach import Coach
from ..models.user import User
from ..extensions import db

def view_coach():
    coaches=Coach.query.all()
    return coaches

def assign_coach(user_id,team_id):
    user_exist= User.query.filter_by(uid=user_id).first()

    if not user_exist:
        return "Invalid User , He/She does not exist in database"
    
    
    if not(user_exist.role=='coach'):
        return "User role is not coach he can't be assigned as a coach"
    
    
    assign=Coach.query.filter_by(user_id=user_id).first()
    if assign:
        return "Coach already assigned to other team"
    team=Coach.query.filter_by(team_id=team_id).first()
    if team:
        return "Team already has Coach"
        
    
    coach=Coach(user_id=user_id,team_id=team_id)

    db.session.add(coach)
    db.session.commit()
    return "coach assigned"

def delete_coach(cid):
    del_details=Coach.query.filter_by(cid=cid).first()

    if not del_details:
        return "Coach does not exist"
    
    db.session.delete(del_details)
    db.session.commit()
    return "Deleted Coach successfully"
