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
    

         
    