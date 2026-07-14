from flask_login import UserMixin
from ..extensions import db

class Team(db.Model,UserMixin):
    __tablename__='team'

    tid=db.Column(db.Integer,primary_key=True)
    team_name=db.Column(db.String, unique=True)
    city=db.Column(db.String)

    trainings=db.relationship("Training",back_populates='team',cascade='all,delete-orphan')

    def __repr__(self):
        return f"Team id of team{self.team_name} is {self.tid} and it is from {self.city} city"
    
    def get_id(self):
        return str(self.tid)