from ..extensions import db

class Training(db.Model):
    __tablename__='training'

    training_id=db.Column(db.Integer, primary_key=True)

    team_id=db.Column(db.Integer,db.ForeignKey("team.tid"),unique=True)
    cid=db.Column(db.Integer,db.ForeignKey("coach.cid"),unique=True)

    title=db.Column(db.String,nullable=False)
    description=db.Column(db.Text)

    date=db.Column(db.Date,nullable=False)
    start_time=db.Column(db.Time,nullable=False)
    end_time=db.Column(db.Time,nullable=False)

    location=db.Column(db.String,nullable=False)

    team=db.relationship("Team",back_populates='trainings')
    coach=db.relationship("Coach",back_populates='trainings')

    def __repr__(self):
        return f" The training id {self.training_id},team id:{self.training_id},coach id :{self.cid},title:{self.title}, description:{self.description}, date:{self.date}, start time:{self.start_time}, end time:{self.end_time}, location:{self.location}"
    