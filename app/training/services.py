from ..extensions import db
from ..models.teams import Team
from ..models.coach import Coach
from ..models.training import Training
def create_training(team_id,cid,title,description,date,start_time,end_time,location):
    check_team=Team.query.filter_by(tid=team_id).first()
    if not check_team:
        return "team does not exist"
    check_coach=Coach.query.filter_by(cid=cid).first()
    if not check_coach:
        return "coach does not exist"
    if check_coach.tid != team_id:
        return "Coach does not belong to this team."
    if end_time<=start_time:
        return "You messed up while setting time"
    
    training=Training(team_id=team_id,
    cid=cid,
    title=title,
    description=description,
    date=date,
    start_time=start_time,
    end_time=end_time,
    location=location)

    db.session.add(training)
    db.session.commit()

    return "Training added successfully"

def view_all_sessions():
    all_sessions=Training.query.all()

    return all_sessions

def view_session(requested_team_id,user_team_id):
    if requested_team_id!=user_team_id:
        return "You can only view your own team's training sessions."
    training_sessions = Training.query.filter_by(team_id=requested_team_id).all()
    if not training_sessions:
        return "No training sessions found."

    return "\n".join(str(session) for session in training_sessions)
    

def view_team_session(requested_team_id):
    check_team_id=Training.query.filter_by(team_id=requested_team_id).all()

    if check_team_id not in requested_team_id:
        return "The Team does not have any Training session right now"
    
    return check_team_id

def update_session(requested_training_id,team_id,cid,title,description,date,start_time,end_time,location):
    check_session=Training.query.filter_by(training_id=requested_training_id).first()

    if not check_session:
        return " Training session does not exist "
    
    if check_session.team_id != team_id:
        return "You cannot update another team's training session."

    if end_time <= start_time:
        return "End time must be after start time."
    
    check_session.team_id=team_id
    check_session.cid=cid
    check_session.title=title
    check_session.description=description
    check_session.date=date
    check_session.start_time=start_time
    check_session.end_time=end_time
    check_session.location=location

    db.session.commit()

    return "Updated session successfully"

def delete_session(requested_training_id,role,team_id):
    check_session=Training.query.filter_by(training_id=requested_training_id).first()

    if not check_session:
        return "No Training session found"
    
    if role == "coach" and check_session.team_id != team_id:
        return "You cannot delete another team's training session."
    
    
    db.session.delete(check_session)
    db.session.commit()

    return "Record deleted successfully"
        
    