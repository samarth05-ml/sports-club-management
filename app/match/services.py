from ..extensions import db
from ..models.teams import Team
from ..models.match import Match


def create_match(requested_h_id,requested_a_id,match_date,match_time,venue):
    home_team_id_check=Team.query.filter_by(tid=requested_h_id).first()

    if not home_team_id_check:
        return "The team you entered as home team does not exist"
    
    away_team_id_check=Team.query.filter_by(tid=requested_a_id).first()

    if not away_team_id_check:
        return " The team you entered as away Team does not exist"
    
    if requested_h_id == requested_a_id:
        return "Home and Away team cannot be the same."
    
    # home_existing_match=Match.query.filter_by(home_team_id=requested_h_id).first()
    # if home_existing_match:
    #     if match_date==home_existing_match.match_date:
    #         if match_time==home_existing_match.match_time:
    #             return "There exist a match for Home team at this time change the timings"

    home_existing_match = Match.query.filter_by(
    home_team_id=requested_h_id,
    match_date=match_date,
    match_time=match_time).first()

    if home_existing_match:
        return "Home team already have match at this time"

    # away_existing_match=Match.query.filter_by(away_team_id=requested_a_id).first()
    # if away_existing_match:
    #     if match_date==away_existing_match.match_date:
    #         if match_time==away_existing_match.match_time:
    #             return "There exist a match for Away team at this time change the timings"
    
    away_existing_match = Match.query.filter_by(
    away_team_id=requested_a_id,
    match_date=match_date,
    match_time=match_time).first()

    if away_existing_match:
        return "Away team already has a match at this time."
        

    match=Match(home_team_id=requested_h_id,away_team_id=requested_a_id,match_date=match_date,match_time=match_time,venue=venue)

    db.session.add(match)
    db.session.commit()

    return "Match created successfully"
        

def view_all_matches():
    matches=Match.query.all()

    return matches

def view_certain_match(requested_mid):
    check_match_id=Match.query.filter_by(mid=requested_mid).first()

    if not check_match_id:
        return "Match does not exist , Maybe you entered wrong match id"
    
    return check_match_id

def update_match(requested_mid,entered_home_score,entered_away_score):
    match_detail=Match.query.filter_by(mid=requested_mid).first()

    if not match_detail:
        return "No matches with entered mid"
    
    if entered_home_score < 0 or entered_away_score < 0:
        return "Scores cannot be negative."

    if entered_home_score > entered_away_score:
        winner_team_id = match_detail.home_team_id
    elif entered_away_score > entered_home_score:
        winner_team_id = match_detail.away_team_id
    else:
        winner_team_id = None

    match_detail.home_score=entered_home_score
    match_detail.away_score=entered_away_score
    match_detail.winner_team_id=winner_team_id

    db.session.commit()
    return "details updated successfully"

def delete_match(requested_mid):
    check_match=Match.query.filter_by(mid=requested_mid).first()

    if not check_match:
        return "there is no matches with this id"
    
    db.session.delete(check_match)
    db.session.commit()

    return "match deleted successfully"
    