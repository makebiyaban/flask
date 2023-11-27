from datetime import datetime
from app1 import db
from sqlalchemy import Column
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	def check_password(self, password):
		return check_password_hash(self.password_hash,password)
	
	id=db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64),index=True,unique=True)
	email = db.Column(db.String(120),index=True,unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<User {}>'.format(self.username)

class Post(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(50))
	body = db.Column(db.String(160))
	timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post {}>'.format(self.body)
