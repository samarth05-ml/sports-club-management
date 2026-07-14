from ..extensions import db
from ..models.players import Player

def assign_player(user_id,team_id,jersey_number,position,dob,height,weight):
    jersey_check=Player.query.filter_by(team_id=team_id,jersey_number=jersey_number).first()

    if jersey_check:
        return " Jersey number exists choose another one "
    
    existing_player=Player.query.filter_by(user_id=user_id).first()
    if existing_player:
        return "Player already exists in some team"
    
    player=Player(user_id=user_id,team_id=team_id,jersey_number=jersey_number,position=position,dob=dob,height=height,weight=weight)

    db.session.add(player)
    db.session.commit()

    return " player assigned "

def view_all_players():
    allp=Player.query.all()

    return allp

def certain_player(pid):
    check_pid=Player.query.filter_by(pid=pid).first()

    if not check_pid:
        return "Player does not exist"
    
    return check_pid

def update_player(pid, team_id, jersey_number, position, dob, height, weight):
    player=Player.query.filter_by(pid=pid).first()

    if not player:
        return "Player does not exist"
    
    jersey_check=Player.query.filter_by(team_id=team_id,jersey_number=jersey_number).first()

    if jersey_check and jersey_check.pid!=player.pid:
        return "Jersey number exists in the team"
    

    player.team_id = team_id
    player.jersey_number = jersey_number
    player.position = position
    player.dob = dob
    player.height = height
    player.weight = weight

    db.session.commit()

    return " Player Update successfully"


def delete_player(pid):
    player_check=Player.query.filter_by(pid=pid).first()

    if not player_check:
        return "Player Does not Exist"
    
    db.session.delete(player_check)
    db.session.commit()

    return "Player deleted successfully but he's still available as user"