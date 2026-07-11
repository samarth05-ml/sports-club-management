from flask_login import UserMixin
from ..extensions import db
class User(db.Model,UserMixin):
    __tablename__='user'

    uid=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,unique=True,nullable=False)
    email=db.Column(db.String,unique=True,nullable=False)
    password=db.Column(db.String,nullable=False)
    role=db.Column(db.Enum("admin", "coach", "player", "medical", name="user_roles"),nullable=False)

    def __repr__(self):
        return f"User with id {self.uid} name:{self.username} and role:{self.role}"
    
    def get_uid(self):
        return str(self.uid)