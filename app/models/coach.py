from ..extensions import db

class Coach(db.Model):
    __tablename__='coach'

    cid=db.Column(db.Integer,primary_key=True)

    user_id=db.Column(db.Integer,
                      db.ForeignKey("user.uid"),
                      unique=True,
                      nullable=False)
    team_id=db.Column(db.Integer,
                      db.ForeignKey("team.tid"),
                      unique=True,
                      nullable=False)
    user=db.relationship("User",backref='coach_profile')
    team=db.relationship("Team",backref='coach')

    def __repr__(self):
        return f"coach id is:{self.cid} , coach user id:{self.user_id} "