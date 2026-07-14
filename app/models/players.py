from ..extensions import db
from ..models.user import User
from ..models.teams import Team

class Player(db.Model):
    __tablename__='player'

    pid = db.Column(db.Integer, primary_key=True)
    uid=db.Column(db.Integer,
                  db.ForeignKey('user.uid'),
                  nullable=False,
                  unique=True)
    tid=db.Column(db.Integer,
                  db.ForeignKey('team.tid'),
                  nullable=False,
                  )
    jersey_number=db.Column(db.Integer,nullable=False)

    position=db.Column(db.String,nullable=False)

    dob=db.Column(db.Date)

    height = db.Column(db.Float)

    weight = db.Column(db.Float)

    user = db.relationship("User", backref="player")

    team = db.relationship("Team", backref="players")

    def __repr__(self):
        return f" player uid{self.uid} , team id:{self.tid}, jersey number:{self.jersey_number} position:{self.position}, dob{self.dob}, weight{self.weight}, height:{self.height} "
    