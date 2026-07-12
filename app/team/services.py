from ..models.teams import Team
from ..extensions import db
from flask import render_template

def create_team(team_name,city):
    team_info=Team.query.filter_by(team_name=team_name).first()

    if team_info:
        return "Team Name already Taken"
    
    team=Team(team_name=team_name,city=city)
    db.session.add(team)
    db.session.commit()

    return "Team added successfully"

def view_team():
    return Team.query.all()

def delete_team(team_name):
    team_info=Team.query.filter_by(team_name=team_name).first()

    if not team_info:
        return "Team not Found"

    db.session.delete(team_info)
    db.session.commit()

    return "Team Deleted Successfully"
 