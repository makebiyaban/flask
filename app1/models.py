from app1 import db
from sqlalchemy import Column

class User(db.Model):
	id=Column(db.Integer, primary_key=True)
	username = Column(db.String(64),index=True,unique=True)
	email = Column(db.String(120),index=True,unique=True)
	password_hash = Column(db.String(128))

	def __repr__(self):
		return '<User {}>'.format(self.username)

class Post(db.Model):
	id=Column(db.Integer,Primary_key=True)
