from app import db
from flask_login import UserMixin

class Deypay_user(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(15), unique=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(80))
	created_ts= db.Column(db.DateTime,  default=db.func.current_timestamp())
	updated_ts= db.Column(db.DateTime,  default=db.func.current_timestamp(),
	                                   onupdate=db.func.current_timestamp())

class Connected_banks(db.Model):
	username = db.Column(db.String(15), primary_key=True)
	bank = db.Column(db.String(80), primary_key=True)
	created_ts= db.Column(db.DateTime,  default=db.func.current_timestamp())
	updated_ts= db.Column(db.DateTime,  default=db.func.current_timestamp(),
	                                   onupdate=db.func.current_timestamp())
	
											
class Tokens(db.Model):
	username = db.Column(db.String(15), primary_key=True)
	bank = db.Column(db.String(80), primary_key=True)
	access_token = db.Column(db.String(1000))
	refresh_token = db.Column(db.String(1000))
	created_ts= db.Column(db.DateTime,  default=db.func.current_timestamp())
	updated_ts= db.Column(db.DateTime,  default=db.func.current_timestamp(),
	                                   onupdate=db.func.current_timestamp())

