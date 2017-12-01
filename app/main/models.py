from .. import db


class Role(db.Model):
    __tablename__ = 'roles'
    roleid = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')


class User(db.Model):
    __tablename__ = 'users'
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))