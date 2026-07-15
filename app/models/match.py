from ..extensions import db

class Match(db.Model):
    __tablename__='match'

    mid=db.Column(db.Integer,primary_key=True)
    home_team_id=db.Column(db.Integer,db.ForeignKey("team.tid"),nullable=False)
    away_team_id=db.Column(db.Integer,db.ForeignKey("team.tid"),nullable=False)

    match_date=db.Column(db.Date,nullable=False)
    match_time=db.Column(db.Time,nullable=False)

    venue=db.Column(db.String,nullable=False)

    home_score=db.Column(db.Integer,nullable=True)
    away_score=db.Column(db.Integer,nullable=True)
    winner_team_id=db.Column(db.Integer,db.ForeignKey('team.tid'),nullable=True)

    def __repr__(self):
        return f"Match Id:{self.mid}, Home team id:{self.home_team_id}, Away team id:{self.away_team_id}, Match date:{self.match_date}, Match Time:{self.match_time}, venue:{self.venue}, home score:{self.home_score}, away score:{self.away_score} winner team id:{self.winner_team_id}"
