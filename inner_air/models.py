from flask_login import UserMixin
from inner_air import bcrypt, login_manager

from inner_air import db


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


"""
    I changed the userID, exerciseID, etc., to id because it is a convention
    and it is a must have thing. Which could also lead to certain problems when
    using UserMixin.
"""


class User(db.Model, UserMixin):
    __tablename__ = 'User.Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    created_time = db.Column(db.DateTime, default=db.func.current_timestamp())

    routines = db.relationship('Routine', backref='user', lazy=True)

    @property
    def hashed_password(self):
        return self.hashed_password

    @hashed_password.setter
    def hashed_password(self, plain_text_password):
        self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class Exercise(db.Model):
    __tablename__ = 'Exercise.Details'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exercise_name = db.Column(db.String(64), nullable=False, unique=True)
    exercise_instructions = db.Column(db.String(256), nullable=False)
    exercise_description = db.Column(db.String(256), nullable=False)
    exercise_length = db.Column(db.Float, nullable=False)
    cumulative_rating = db.Column(db.Float)
    category_id = db.Column(db.Integer, nullable=False)

    routines = db.relationship('Routine', backref='exercise', lazy=True)


class Routine(db.Model):
    __tablename__ = 'Users.Routines'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.Users.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('Exercise.Details.id'), nullable=False)
